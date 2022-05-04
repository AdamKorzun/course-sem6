
# class DbRequestThread(threading.Thread):
#     def __init__(threadID, name, counter):
#         thread.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run():
#         print('Модуль для работы с параллельным кодом свою работу сделал (:')

#
# class ConfigManager:
#     def __init__(self, json_config_path):
#         with open(json_config_path, 'r') as file:
#             json_config = json.load(file)
#         self.db_host = json_config['db_host']
#         self.db_user = json_config['db_user']
#         self.db_password = json_config['db_password']
#         self.db_name = json_config['db_name']
#         self.users_table_name = json_config['users_table']
#         self.ip = json_config['ip']
#         self.port = json_config['port']
#
# def create_connection(host_name, user_name, user_password, db_name):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host = host_name,
#             user = user_name,
#             passwd=user_password,
#             database=db_name
#         )
#     except Exception as e:
#         print(e)
#     return connection
