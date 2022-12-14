from dotenv import load_dotenv
load_dotenv()
from app.models import Employee, Menu, MenuItem, MenuItemType
from app import app, db


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234,
                        password="password")
    db.session.add(employee)

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    db.session.add(beverages)


    db.session.add(entrees)


    db.session.add(sides)


    db.session.add(dinner)


    db.session.add(fries)


    db.session.add(drp)


    db.session.add(jambalaya)
    db.session.commit()

    print([x.name for x in dinner.menu_items])
