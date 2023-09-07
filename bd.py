import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_product_description():
    # Define la conexión a la base de datos (reemplaza 'sqlite:///tu_base_de_datos.db' por tu conexión real)
    engine = create_engine('sqlite:///tu_base_de_datos.db')

    # Define la clase Product y ProductDescription como modelos
    Base = declarative_base()

    class Product(Base):
        __tablename__ = 'Product'
        ProductID = Column(Integer, primary_key=True)
        ProductName = Column(String)

    class ProductDescription(Base):
        __tablename__ = 'ProductDescription'
        ProductID = Column(Integer, primary_key=True)
        ProductDescription = Column(String)

    # Crea una sesión para interactuar con la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Consulta SQL equivalente al procedimiento
        result = session.query(Product.ProductID, Product.ProductName, ProductDescription.ProductDescription).\
            join(ProductDescription, Product.ProductID == ProductDescription.ProductID).all()

        return result
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cierra la sesión
        session.close()

# Llama a la función y obtén los resultados
results = get_product_description()

# Imprime los resultados
for row in results:
    print(f"ProductID: {row.ProductID}, ProductName: {row.ProductName}, ProductDescription: {row.ProductDescription}")


