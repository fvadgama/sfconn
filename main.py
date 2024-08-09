
import salesforceconnector as sfc

# Connect to SF
connector = sfc.SalesforceConnector('<USERNAME>', '<PASSWORD',
                                    '<SECURITYTOKEN>')
connector.connect()

# Query Accounts data
accounts = connector.query("SELECT Id, Name FROM Account limit 10")
print(accounts)

# Create an Account
#acctid = connector.create('Account', {'Name': 'ABC Company'})
#print(f"New Account ID: {acctid}")

# Update the Account
#acctid = '001aj00000T4l2wAAB'
#connector.update('Account', acctid, {'Name': 'XYZ Company'})

# Delete the Account
#connector.delete('Account', new_account_id)