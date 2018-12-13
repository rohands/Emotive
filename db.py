import psycopg2

try:
    connection = psycopg2.connect(user = "rohands",
                                  password = "rohan",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "emotive")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



#create table users(phone int primary key, name varchar(255) not null,first_message varchar(3000) not null, pos_message varchar(3000) not null, neg_message varchar(3000) not null);
#insert into users(phone,name,first_message,pos_message,neg_message) values (2132928086,'Rohan','NA','NA','NA');