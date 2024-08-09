from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceAuthenticationFailed


class SalesforceConnector:
    def __init__(self, username, password, security_token, domain='login'):
        """
        Initialize the SalesforceConnector class.

        :param username: Salesforce username
        :param password: Salesforce password
        :param security_token: Salesforce security token
        :param domain: Salesforce domain (default is 'login')
        """
        self.username = username
        self.password = password
        self.security_token = security_token
        self.domain = domain
        self.sf = None

    def connect(self):
        """
        Establish a connection to Salesforce.
        """
        try:
            self.sf = Salesforce(
                username=self.username,
                password=self.password,
                security_token=self.security_token,
                domain=self.domain
            )
            print("Connected to Salesforce successfully.")
        except SalesforceAuthenticationFailed as e:
            print(f"Failed to connect to Salesforce: {e}")
            raise

    def query(self, soql_query):
        """
        Execute a SOQL query.

        :param soql_query: The SOQL query string
        :return: The query result as a dictionary
        """
        if not self.sf:
            raise ConnectionError("Salesforce is not connected.")

        try:
            result = self.sf.query(soql_query)
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            raise

    def create(self, object_name, data):
        """
        Create a new record in Salesforce.

        :param object_name: The name of the Salesforce object (e.g., 'Account')
        :param data: A dictionary containing the data for the new record
        :return: The ID of the newly created record
        """
        if not self.sf:
            raise ConnectionError("Salesforce is not connected.")

        try:
            result = self.sf.__getattr__(object_name).create(data)
            return result['id']
        except Exception as e:
            print(f"Error creating record: {e}")
            raise

    def update(self, object_name, record_id, data):
        """
        Update an existing record in Salesforce.

        :param object_name: The name of the Salesforce object (e.g., 'Account')
        :param record_id: The ID of the record to update
        :param data: A dictionary containing the updated data
        """
        if not self.sf:
            raise ConnectionError("Salesforce is not connected.")

        try:
            self.sf.__getattr__(object_name).update(record_id, data)
            print(f"Record {record_id} updated successfully.")
        except Exception as e:
            print(f"Error updating record: {e}")
            raise

    def delete(self, object_name, record_id):
        """
        Delete a record in Salesforce.

        :param object_name: The name of the Salesforce object (e.g., 'Account')
        :param record_id: The ID of the record to delete
        """
        if not self.sf:
            raise ConnectionError("Salesforce is not connected.")

        try:
            self.sf.__getattr__(object_name).delete(record_id)
            print(f"Record {record_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
            raise


