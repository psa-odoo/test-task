import csv
from tkinter import *

#3 Form fields
fields = ('Name', 'Email', 'Phone')

# Define form and assign positions of fields and textbox
def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

# Main Logic regarding Read and Write operations has been done here.
def csv_operations(self):
    # defined variables and assigning values to them
    name = self['Name'].get() if self['Name'] else ''
    email = self['Email'].get() if self['Email'] else ''
    phone = self['Phone'].get() if self['Phone'] else ''

    # Open and read the Contact_list.csv file
    contact_read_csv = open('contact_list.csv', 'r', newline='')
    contact_read_obj = csv.reader(contact_read_csv)

    # Open and read the Lead.csv file
    lead_read_csv = open('Lead.csv', 'r', newline='')
    lead_read_obj = csv.reader(lead_read_csv)

    #set default
    found = 0
    lead_found = 0

    for row in contact_read_obj:
        if row[0] == name or row[1] == email or row[2] == phone:
            found = 1
            break
        else:
            found = 0
    if found == 0:
        for row in lead_read_obj:
            if row[0] == name or row[1] == email or row[2] == phone:
                lead_found = 1
                break
            else:
                found = 0

    lead_read_csv_line = open('Lead.csv', 'r', newline='')
    lead_read_obj_line = csv.reader(lead_read_csv_line)

    lines = []
    for row in lead_read_obj_line:
        if not(row[1].strip() == email.strip()) or not(row[2].strip() == phone.strip()):
            lines.append(row)

    csv_lead_writer = open('Lead.csv', 'w', newline='')
    csv_lead_obj = csv.writer(csv_lead_writer)
    csv_lead_obj.writerows(lines)

    if found == 0 or lead_found == 1:
        new_data_list = [name, email, phone]
        new_data_disc = [{'name': name, 'email': email, 'phone': phone}]
        with open('contact_list.csv', 'a+', newline='') as write_obj:
            csv_writer = csv.writer(write_obj)
            csv_writer.writerow(new_data_list)
            print('Contact created...')
    else:
        print('Contact already exists!!!')

if __name__ == '__main__':
    root = Tk()
    root.title("Welcome to IT Perfectionist's Webinar")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e = ents: fetch(e)))
    b1 = Button(root, text = 'Submit',
      command=(lambda e = ents: csv_operations(e)))
    b1.pack(side = RIGHT, padx = 5, pady = 5)

    root.mainloop()
