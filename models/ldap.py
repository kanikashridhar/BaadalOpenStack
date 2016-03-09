import ConfigParser


config = ConfigParser.ConfigParser()


ldap_host = config.get('ldap', 'ldap_host')
ldap_dn = config.get('ldap', 'ldap_dn')
ldap_base_dn = config.get('ldap', 'ldap_base_dn')
ldap_admin_dn = config.get('ldap', 'ldap_admin_dn')
ldap_admin_password = config.get('ldap', 'ldap_admin_password')


ldap = BaadalLDAP(ldap_host, ldap_base_dn, ldap_admin_dn,
                  ldap_admin_password)
