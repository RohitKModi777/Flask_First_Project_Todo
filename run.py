from app import create_app, mongo

app = create_app()

if __name__ == "__main__":

    with app.app_context():
        mongo.db.users  
        mongo.db.tasks


    app.run()
