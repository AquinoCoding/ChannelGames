from db import engine
from sqlalchemy.orm import sessionmaker
from db import User

global session

Session = sessionmaker(bind=engine)
session = Session()

class DBControllers:
      
      # Para adicionar passos os paramentros da add conforme
      # a Class do Banco de dados
      def InsertData(databaseInsert):      
            session = Session()
            session.add(databaseInsert)
            session.commit()
      
      # Para checar informações passo o nome da TABLE "databaseVerification"
      # E instacio o nome do objeto que será buscado "instance"
      def SelectData(self, data):

            def __init__(self):
                  self.data = data
                  
            def filterId(self, instance):
                  query_user = session.query(self.data).filter_by(name=instance)
                  print(query_user)

            def filterName(self, instance):
                  query_user = session.query(self.data).filter_by(name=instance)
                  print(query_user)
            
            def filterAll(self, instance):
                  for instance in session.query(self.data).order_by(self.data.id):
                        print(instance.id, instance)

      
      # Edição feita apenas por instacia de ID
      def UpdateData(databaseUpdate, instance):

            user = session.query(databaseUpdate).filter_by(id=instance).first()

            def UpdateName(user):
                  newupdateValue = input()
                  user.name = str(newupdateValue)
                  print(session.dirty)
                  session.commit()
                  print('Update sucess Name')
            
            def UpdatePassword(user):
                  newupdateValue = input()
                  user.senha = str(newupdateValue)
                  print(session.dirty)
                  session.commit()
                  print('Update sucess Password')
      
      #InsertData(User(name='Lucas', senha='123'))
      SelectData()
      SelectData.filterName(User, 'admin')
      #UpdateData(User, 21, Camp)
