from project import create_app

if __name__ == '__main__':
  app = create_app()
  app.run(host = '127.0.0.0', port = 8001, debug=False) #DO  NOT USE 0.0.0.0 its a f###### open address

