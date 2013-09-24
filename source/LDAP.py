
import ldap

class LDAP(object):
  def __init__(self):
    self.l = None

  def connect(self, uri):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 2)
    ldap.set_option(ldap.OPT_REFERRALS, 0)
    self.l = ldap.initialize(uri)
    self.l.protocol_version = ldap.VERSION3
    return self.l

  def bind(self, dn, password):
    self.l.simple_bind(dn, password)

  def search(self,ldap_filter="(objectClass=*)",baseDN=None,attrs=None,scope=ldap.SCOPE_SUBTREE):
        
        try:
            ldap_result_id = self.l.search(baseDN, scope, ldap_filter, attrs)
            ldap_result = {}
            while 1:
                result_type, result_data = self.l.result(ldap_result_id, 0)
                if result_type == ldap.RES_SEARCH_RESULT:
                    break
                elif result_type == ldap.RES_SEARCH_ENTRY:
                    ldap_result[result_data[0][0]] = result_data[0][1]
                elif result_type == ldap.RES_SEARCH_REFERENCE:
                    dn = result_data[0][1][0].split('/', 3)[3].split("?")[0]
                    attr, value = dn.split(',')[0].split('=')
                    ldap_result[dn] = {'ref': [result_data[0][1][0]], 'objectClass': ['referral', 'extensibleObject'], attr: [value]}
                else:
                    print "ERROR: result type not implemented. %s" % result_type
            return ldap_result
        except ldap.LDAPError, e:
            #self.parse_exception("LDAPError", e)
            if e[0]["desc"] == "Size limit exceeded":
                return ldap_result

    