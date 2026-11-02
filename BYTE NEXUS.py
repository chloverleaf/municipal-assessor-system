requests = []
request_number = 1
resident_accounts = [] 

documents = ["Certified True Copy of Tax Declaration","Certification of Property Ownership","Tax Clearance"]

requirements = [["Valid ID", "Request Form"],["Valid ID", "Request Form"],["Valid ID", "Request Form"]]

statuses = ["Submitted","Under Review","Action Required","Ready for Processing","Ready for Release","Released"]

appointment_statuses = ["Booked","Completed","Cancelled"]

appointments = []

slots = [["October 19, 2026", "9:00 AM - 9:30 AM", 5, 0],["October 19, 2026", "8:30 AM - 9:30 AM", 5, 0],["October 20, 2026", "9:00 AM - 9:30 AM" , 5, 0]]

def show_available_documents():
    print()
    print("                         ✦ AVAILABLE DOCUMENTS ✦")
    print("--------------------------------------------------------------------------------")
    print("| No. |             Document Requested              |         Requirements     |")
    print("--------------------------------------------------------------------------------")

    i = 0

    for document in documents:
        requirement_list = ""

        for requirement in requirements[i]:
            if requirement_list == "":
                requirement_list = requirement
            else:
                requirement_list = requirement_list + ", " + requirement

        print()
        print("|", i + 1, "|", document)
        print("      Requirements:", requirement_list)
        print("--------------------------------------------------------------------------------")

        i = i + 1

    print("--------------------------------------------------------------------------------") 

def check_request_status(username):
    print()
    print("                 ✦ REQUEST TRACKING ✦")
    print("======================================================================")

    while True:
        reference_no = input("Enter reference number (or B to go back): ")

        if reference_no == "B" or reference_no == "b":
            return

        found = False

        for request in requests:
            if request[0] == reference_no:
                if request[1] == username:
                    found = True
                    break

        if found:
            break

        print()
        print("Request not found in your account.")
        print("Please check your reference number.")
        print("======================================================================")

    print()
    print("                    ✦ REQUEST DETAILS ✦")
    print("======================================================================")
    print("Reference Number       :", request[0])
    print("Requester Name         :", request[2])
    print("Property Owner         :", request[3])
    print("Document Requested     :", request[4])
    print("Tax Declaration Number :", request[5])
    print("Property Location      :", request[6])
    print("Purpose                :", request[7])
    print("----------------------------------------------------------------------")
    print("Request Status         :", request[8])
    print("----------------------------------------------------------------------")

    if request[8] == "Submitted":
        print("Next Step              : Your request is waiting for staff review.")

    elif request[8] == "Under Review":
        print("Next Step              : Staff are reviewing your request.")

    elif request[8] == "Action Required":
        print("Next Step              : Please address the missing requirements.")

    elif request[8] == "Ready for Processing":
        print("Next Step              : Your requirements have been verified.")

    elif request[8] == "Ready for Release":
        print("Next Step              : Your document is ready for release.")

    elif request[8] == "Released":
        print("Next Step              : Your document has been released.")

    print("----------------------------------------------------------------------")

    if request[9] == "":
        print("Staff Instructions     : No staff instructions recorded.")
    else:
        print("Staff Instructions     :", request[9])

    print("======================================================================")
    
 
def book_appointment(username):
    eligible_requests = []

    for request in requests:
        if request[1] == username:
            if request[8] == "Submitted" or request[8] == "Action Required":
                has_active_appointment = False

                for appointment in appointments:
                    if appointment[0] == request[0]:
                        if appointment[4] == "Booked":
                            has_active_appointment = True

                if has_active_appointment == False:
                    eligible_requests.append(request)

    if eligible_requests == []:
        print()
        print("You have no requests available for appointment booking.")
        print("Requests must be marked Submitted or Action Required")
        print("and must not have an active appointment.")
        print("======================================================================")
        input("Press Enter to go back.")
        return

    print()
    print("                ✦ ELIGIBLE DOCUMENT REQUESTS ✦")
    print("============================================================")

    i = 0

    for request in eligible_requests:
        print()
        print("REQUEST " + str(i + 1))
        print("------------------------------------------------------------")
        print("Reference Number  :", request[0])
        print("Document Requested:", request[4])
        print("Property Owner    :", request[3])
        print("Request Status    :", request[8])
        print("------------------------------------------------------------")

        i = i + 1

    print()
    print("[B] - Back")
    print("============================================================")
    print("Total Requests:", i)
    print("============================================================")

    choice = input("Select a request: ")

    while True:
        valid_choice = False

        if choice == "B" or choice == "b":
            valid_choice = True
        else:
            i = 1

            for request in eligible_requests:
                if choice == str(i):
                    valid_choice = True
                    break

                i = i + 1

        if valid_choice == True:
            break

        print("Invalid choice. Please select a listed request or B.")
        choice = input("Select a request: ")

    if choice == "B" or choice == "b":
        print("Appointment booking cancelled.")
        return

    selected_request = eligible_requests[int(choice) - 1]
    reference_no = selected_request[0]

    print()
    print("Request Reference:", reference_no)
    print("Document Requested:", selected_request[4])
    print("Request Status:", selected_request[8])
    print("======================================================================")

    while True:
        available_slots = 0

        for slot in slots:
            if slot[3] < slot[2]:
                available_slots = available_slots + 1

        if available_slots == 0:
            print()
            print("Sorry, all appointment slots are full.")
            print("Please try again later.")
            print("======================================================================")
            return

        print()
        print("                  ✦ AVAILABLE APPOINTMENT SLOTS ✦")
        print("===============================================================")
        print("| Slot No. |       Date       |        Time       | Available |")
        print("---------------------------------------------------------------")

        i = 0

        for slot in slots:
            available = slot[2] - slot[3]

            print(
                "|    " + str(i + 1) + "     | "
                + slot[0] + " | "
                + slot[1] + " |     "
                + str(available) + "     |"
            )

            i = i + 1

        print("===============================================================")
        print("[B] - Back")
        print("===============================================================")

        slot_number = input("Select an appointment slot: ")

        while True:
            valid_slot = False

            if slot_number == "B" or slot_number == "b":
                valid_slot = True
            else:
                i = 1

                for slot in slots:
                    if slot_number == str(i):
                        valid_slot = True
                        break

                    i = i + 1

            if valid_slot == True:
                break

            print("Invalid choice. Please select a listed slot or B.")
            slot_number = input("Select an appointment slot: ")

        if slot_number == "B" or slot_number == "b":
            print("Appointment booking cancelled.")
            return

        selected_slot = slots[int(slot_number) - 1]

        if selected_slot[3] < selected_slot[2]:
            break

        print()
        print("That appointment slot is full.")
        print("Please choose another available slot.")

    appointment = [
        reference_no,
        username,
        selected_slot[0],
        selected_slot[1],
        "Booked"
    ]

    appointments.append(appointment)
    selected_slot[3] = selected_slot[3] + 1

    print()
    print("Appointment booked successfully!")
    print("Request Reference:", reference_no)
    print("Date:", selected_slot[0])
    print("Time:", selected_slot[1])
    print("Appointment Status: Booked")
    print("================================================================")

def cancel_appointment(username):
    active_appointments = []

    for appointment in appointments:
        if appointment[1] == username:
            if appointment[4] == "Booked":
                active_appointments.append(appointment)

    if active_appointments == []:
        print("You have no active appointments to cancel.")
        print("======================================================================")
        return

    print()
    print("                  ✦ YOUR ACTIVE APPOINTMENTS ✦")
    print("======================================================================")

    i = 0

    for appointment in active_appointments:
        reference_no = appointment[0]
        document = "Not Available"

        for request in requests:
            if request[0] == reference_no:
                document = request[4]
                break

        print()
        print("APPOINTMENT " + str(i + 1))
        print("----------------------------------------------------------------------")
        print("Reference Number   :", reference_no)
        print("Document Requested :", document)
        print("Appointment Date   :", appointment[2])
        print("Appointment Time   :", appointment[3])
        print("Appointment Status :", appointment[4])
        print("----------------------------------------------------------------------")

        i = i + 1

    print()
    print("[B] - Back")
    print("======================================================================")
    print("Total Appointments:", i)
    print("======================================================================")

    choice = input("Select an appointment to cancel: ")

    while True:
        valid_choice = False

        if choice == "B" or choice == "b":
            valid_choice = True
        else:
            i = 1

            for appointment in active_appointments:
                if choice == str(i):
                    valid_choice = True
                    break

                i = i + 1

        if valid_choice == True:
            break

        print("Invalid choice. Please select a listed appointment or B.")
        choice = input("Select an appointment to cancel: ")

    if choice == "B" or choice == "b":
        print("Appointment cancellation cancelled.")
        return

    selected_appointment = active_appointments[int(choice) - 1]

    print()
    print("======================================================================")
    print("               ✦ CONFIRM APPOINTMENT CANCELLATION ✦")
    print("======================================================================")
    print("Reference Number   :", selected_appointment[0])
    print("Appointment Date   :", selected_appointment[2])
    print("Appointment Time   :", selected_appointment[3])
    print("Appointment Status :", selected_appointment[4])
    print("----------------------------------------------------------------------")
    print("[1] - Confirm Cancellation")
    print("[2] - Keep Appointment")
    print("======================================================================")

    confirmation = input("Enter your choice: ")

    while not (confirmation == "1" or confirmation == "2"):
        print("Invalid choice. Please enter 1 or 2.")
        confirmation = input("Enter your choice: ")

    if confirmation == "2":
        print("Your appointment remains booked.")
        print("======================================================================")
        return

    selected_appointment[4] = "Cancelled"

    for slot in slots:
        if slot[0] == selected_appointment[2]:
            if slot[1] == selected_appointment[3]:
                if slot[3] > 0:
                    slot[3] = slot[3] - 1
                break

    print()
    print("======================================================================")
    print("Appointment cancelled successfully.")
    print("Appointment Status: Cancelled")
    print("Your document request has been preserved.")
    print("You may book another appointment if your request")
    print("is still eligible.")
    print("======================================================================")

def my_appointments(username):
    print()
    print("     ✦ MY APPOINTMENTS ✦")
    print("------------------------------")

    found = False

    for appointment in appointments:
        if appointment[1] == username:
            print()
            print("Request Reference:", appointment[0])

            for request in requests:
                if request[0] == appointment[0]:
                    print("➜", request[4])

            print("Date:", appointment[2])
            print("Time:", appointment[3])
            print("Appointment Status:", appointment[4])
            print("------------------------------")

            found = True

    if found == False:
        print("You have no appointments yet.")
        print("------------------------------")

def my_appointments(username):
    print()
    print("                    ✦ MY APPOINTMENTS ✦")
    print("============================================================")

    total_appointments = 0

    for appointment in appointments:
        if appointment[1] == username:
            total_appointments += 1

            reference_no = appointment[0]
            document = "Not Available"

            for request in requests:
                if request[0] == reference_no:
                    document = request[4]
                    break

            print()
            print("APPOINTMENT", total_appointments)
            print("------------------------------------------------------------")
            print("Reference Number  :", reference_no)
            print("Document Requested:", document)
            print("Appointment Date  :", appointment[2])
            print("Appointment Time  :", appointment[3])
            print("Appointment Status:", appointment[4])
            print("------------------------------------------------------------")

    if total_appointments == 0:
        print()
        print("You have no appointments yet.")

    print()
    print("============================================================")
    print("Total Appointments:", total_appointments)
    print("============================================================")

def my_requests_and_appointments(username):
    while True:
        print()
        print("✦ MY REQUESTS AND APPOINTMENTS ✦")
        print("---------------------------------")
        print("[1] - View My Requests")
        print("[2] - Track Request Status")
        print("[3] - View My Appointments")
        print("[4] - Back")
        print("---------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            my_requests(username)

        elif choice == "2":
            check_request_status(username)

        elif choice == "3":
            my_appointments(username)

        elif choice == "4":
            return

        else:
            print("Please enter a valid choice.")

def book_new_request(request_number, username, request):
    while True:
        available_slots = 0

        for slot in slots:
            if slot[3] < slot[2]:
                available_slots = available_slots + 1

        if available_slots == 0:
            print()
            print("Sorry, all appointment slots are full.")
            print("Your request has not been submitted.")
            return request_number

        print()
        print("                 ✦ AVAILABLE APPOINTMENT SLOTS ✦")
        print("-------------------------------------------------------------------")
        print("| Slot No. |       Date       |        Time       |Available Slots|")
        print("-------------------------------------------------------------------")

        i = 0

        for slot in slots:
            available = slot[2] - slot[3]

            if available == 0:
                available_text = "0"
            else:
                available_text = str(available)

            if available_text == "0":
                print(
                    "|    " + str(i + 1) + "     | "
                    + slot[0] + " | "
                    + slot[1] + " |"
                    + "      0       |"
                )
            else:
                print(
                    "|    " + str(i + 1) + "     | "
                    + slot[0] + " | "
                    + slot[1] + " |"
                    + "        " + available_text + "    |"
                )

            i = i + 1

        print("-------------------------------------------------------------------")
        print("Enter the slot number you prefer (or B to cancel):")

        choice = input("Your choice: ")

        while not (
            choice == "1"
            or choice == "2"
            or choice == "3"
            or choice == "B"
            or choice == "b"
        ):
            print("Please enter 1, 2, 3, or B.")
            choice = input("Your choice: ")

        if choice == "B" or choice == "b":
            print("Appointment booking cancelled.")
            print("Your request has not been submitted.")
            return request_number

        selected_slot = slots[int(choice) - 1]

        if selected_slot[3] >= selected_slot[2]:
            print()
            print("Sorry, that appointment slot is already  .")
            print("Please choose another available slot.")
        else:
            reference_no = "MAO-" + str(request_number).zfill(3)
            request[0] = reference_no

            requests.append(request)

            appointment = [
                reference_no,
                username,
                selected_slot[0],
                selected_slot[1],
                "Booked"
            ]

            appointments.append(appointment)

            selected_slot[3] = selected_slot[3] + 1

            print()
            print("✦ APPOINTMENT BOOKED SUCCESSFULLY ✦")
            print("-----------------------------------")
            print("Reference Number:", reference_no)
            print("Document Requested:", request[4])
            print("Appointment Date:", selected_slot[0])
            print("Appointment Time:", selected_slot[1])
            print("Request Status: Submitted")
            print("Please save your reference number.")
            print("-----------------------------------")

            return request_number + 1

def book_new_request(request_number, username, request):
    while True:
        available_slots = 0

        for slot in slots:
            if slot[3] < slot[2]:
                available_slots = available_slots + 1

        if available_slots == 0:
            print()
            print("Sorry, all appointment slots are full.")
            print("Your request has not been submitted.")
            return request_number

        print()
        print("                 ✦ AVAILABLE APPOINTMENT SLOTS ✦")
        print("-------------------------------------------------------------------")
        print("| Slot No. |       Date       |        Time       |Available Slots|")
        print("-------------------------------------------------------------------")

        i = 0

        for slot in slots:
            available = slot[2] - slot[3]

            if available == 0:
                available_text = "0"
            else:
                available_text = str(available)

            print(
                "|    " + str(i + 1) + "     | "
                + slot[0] + " | "
                + slot[1] + " |"
                + "       " + available_text + "       |"
            )

            i = i + 1

        print("-------------------------------------------------------------------")
        print("Enter the slot number you prefer (or B to cancel):")

        choice = input("Your choice: ")

        slot_count = 0

        for slot in slots:
            slot_count = slot_count + 1

        valid_choice = False

        while valid_choice == False:
            if choice == "B" or choice == "b":
                break

            if choice.isdigit():
                if int(choice) >= 1 and int(choice) <= slot_count:
                    valid_choice = True

            if valid_choice == False:
                print("Invalid choice. Please enter a listed slot number or B.")
                choice = input("Your choice: ")

        if choice == "B" or choice == "b":
            print("Appointment booking cancelled.")
            print("Your request has not been submitted.")
            return request_number

        selected_slot = slots[int(choice) - 1]

        if selected_slot[3] >= selected_slot[2]:
            print()
            print("Sorry, that appointment slot is already full.")
            print("Please choose another available slot.")

        else:
            reference_no = "MAO-" + str(request_number).zfill(3)
            request[0] = reference_no

            requests.append(request)

            appointment = [
                reference_no,
                username,
                selected_slot[0],
                selected_slot[1],
                "Booked"
            ]

            appointments.append(appointment)

            selected_slot[3] = selected_slot[3] + 1

            print()
            print("✦ APPOINTMENT BOOKED SUCCESSFULLY ✦")
            print("------------------------------------")
            print("Reference Number:", reference_no)
            print("Document Requested:", request[4])
            print("Appointment Date:", selected_slot[0])
            print("Appointment Time:", selected_slot[1])
            print("Request Status: Submitted")
            print("Appointment Status: Booked")
            print("Please save your reference number.")
            print("------------------------------------")

            return request_number + 1

def show_available_documents():
    print()
    print("                    ✦ AVAILABLE DOCUMENTS ✦")
    print("--------------------------------------------------------------------------")
    print("| No. | Document Requested                     | Requirements            |")
    print("--------------------------------------------------------------------------")

    i = 0

    for document in documents:
        requirement_list = ""

        for requirement in requirements[i]:
            if requirement_list == "":
                requirement_list = requirement
            else:
                requirement_list = requirement_list + ", " + requirement

        if i == 0:
            print("|  1  | Certified True Copy of Tax Declaration | Valid ID, Request Form  |")

        elif i == 1:
            print("|  2  | Certification of Property Ownership    | Valid ID, Request Form  |")

        else:
            print("|  3  | Tax Clearance                          | Valid ID, Request Form  |")

        print("--------------------------------------------------------------------------")

        i = i + 1
          
def record_request(request_number, username):
    print()
    print(" ✦ SUBMIT DOCUMENT REQUEST ✦")
    print("------------------------------")

    name = ""

    for account in resident_accounts:
        if account[0] == username:
            name = account[2]

    if name == "":
        print("Unable to retrieve your account name.")
        print("------------------------------")
        return request_number

    print("Requester Name:", name)

    print()
    print("Available Documents:")
    print("------------------------------")

    i = 0

    for document in documents:
        print(i + 1, "-", document)
        i = i + 1

    print()

    document_number = input(
        "Enter document number (or B to go back): "
    )

    while not (
        document_number == "1"
        or document_number == "2"
        or document_number == "3"
        or document_number == "B"
        or document_number == "b"
    ):
        print("Please enter a valid document number.")
        document_number = input(
            "Enter document number (or B to go back): "
        )

    if document_number == "B" or document_number == "b":
        return request_number

    document = documents[int(document_number) - 1]
    document_index = int(document_number) - 1

    print()

    owner_name = input("Enter property owner's full name: ")

    while owner_name.strip() == "":
        print("Please enter the property owner's full name.")
        owner_name = input("Enter property owner's full name: ")

    print()

    tax_number = input(
        "Enter Tax Declaration Number (or press Enter if unknown): "
    )

    print()

    property_location = input(
        "Enter property location or barangay: "
    )

    while property_location.strip() == "":
        print("Please enter the property location or barangay.")
        property_location = input(
            "Enter property location or barangay: "
        )

    print()

    purpose = input("Why do you need this document? ")

    while purpose.strip() == "":
        print("Please enter the purpose of your request.")
        purpose = input("Why do you need this document? ")

    request = [
        "",
        username,
        name,
        owner_name,
        document,
        tax_number,
        property_location,
        purpose,
        "Submitted",
        ""
    ]

    print()
    print("➜", document)
    print("Requirements:")

    for requirement in requirements[document_index]:
        print("   •", requirement)

    print("------------------------------")
    print("An appointment is required to submit your request.")
    print("Your request will be saved after booking successfully.")
    print("------------------------------")

    request_number = book_new_request(
        request_number, username, request
    )

    return request_number

def request_monitoring():
    while True:
        print()
        print("                 ✦ REQUEST MONITORING ✦")
        print("============================================================")

        counts = [0, 0, 0, 0, 0, 0]

        for request in requests:
            i = 0

            for status in statuses:
                if request[8] == status:
                    counts[i] = counts[i] + 1

                i = i + 1

        total = 0

        for count in counts:
            total = total + count

        print("Total Requests:", total)
        print("------------------------------------------------------------")

        i = 0

        for status in statuses:
            print(status + ":", counts[i])
            i = i + 1

        print("============================================================")
        print("[1] - View All Requests")
        print("[2] - Find Request")
        print("[3] - View Requests by Status")
        print("[4] - Back")
        print("============================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            if requests == []:
                print()
                print("No document requests have been recorded.")
            else:
                print()
                print("                 ✦ ALL DOCUMENT REQUESTS ✦")
                print("============================================================")

                request_number = 0

                for request in requests:
                    request_number = request_number + 1

                    print()
                    print("REQUEST", request_number)
                    print("------------------------------------------------------------")
                    print("Reference Number          :", request[0])
                    print("Requester                 :", request[2])
                    print("Property Owner            :", request[3])
                    print("Document Requested        :", request[4])
                    print("Tax Declaration Number    :", request[5])
                    print("Property Location         :", request[6])
                    print("Purpose                   :", request[7])
                    print("Request Status            :", request[8])
                    print("Staff Instructions        :", request[9])
                    print("------------------------------------------------------------")

                print()
                print("Total Requests:", request_number)
                print("============================================================")

        elif choice == "2":
            reference_no = input("Enter reference number: ")

            found = False

            for request in requests:
                if request[0] == reference_no:
                    print()
                    print("                 ✦ REQUEST DETAILS ✦")
                    print("============================================================")
                    print("Reference Number          :", request[0])
                    print("Requester                 :", request[2])
                    print("Property Owner            :", request[3])
                    print("Document Requested        :", request[4])
                    print("Tax Declaration Number    :", request[5])
                    print("Property Location         :", request[6])
                    print("Purpose                   :", request[7])
                    print("Request Status            :", request[8])
                    print("Staff Instructions        :", request[9])
                    print("============================================================")

                    found = True
                    break

            if found == False:
                print()
                print("Request not found.")

        elif choice == "3":
            print()
            print("                 ✦ FILTER REQUESTS BY STATUS ✦")
            print("============================================================")
            print("Available Statuses:")

            i = 0

            for status in statuses:
                print(i + 1, "-", status)
                i = i + 1

            status_number = input("Enter status number: ")

            while not (
                status_number == "1"
                or status_number == "2"
                or status_number == "3"
                or status_number == "4"
                or status_number == "5"
                or status_number == "6"
            ):
                print("Please enter a valid status number.")
                status_number = input("Enter status number: ")

            selected_status = statuses[int(status_number) - 1]

            print()
            print("Requests with Status:", selected_status)
            print("============================================================")

            found = False
            request_number = 0

            for request in requests:
                if request[8] == selected_status:
                    request_number = request_number + 1


                    print()
                    print("REQUEST", request_number)
                    print("------------------------------------------------------------")
                    print("Reference Number    :", request[0])
                    print("Requester           :", request[2])
                    print("Document Requested  :", request[4])
                    print("Property Location   :", request[6])
                    print("Request Status      :", request[8])
                    print("------------------------------------------------------------")

                    found = True

            if found == False:
                print("No requests found with this status.")

            print()
            print("============================================================")

        elif choice == "4":
            return

        else:
            print("Please enter a valid choice."
                )

def request_monitoring():
    while True:
        print()
        print("                ✦ REQUEST MONITORING SUMMARY ✦")
        print("============================================================")

        counts = [0, 0, 0, 0, 0, 0]

        for request in requests:
            i = 0

            for status in statuses:
                if request[8] == status:
                    counts[i] = counts[i] + 1

                i = i + 1

        total = 0

        for count in counts:
            total = total + count

        print("Total Requests:", total)
        print("------------------------------------------------------------")

        i = 0

        for status in statuses:
            print(status + ":", counts[i])
            i = i + 1

        print("============================================================")
        print("[1] - View All Requests")
        print("[2] - Find Request")
        print("[3] - View Requests by Status")
        print("[4] - Back")
        print("============================================================")

        choice = input("Enter your choice: ")

        while not (
            choice == "1"
            or choice == "2"
            or choice == "3"
            or choice == "4"
        ):
            print("Please enter a valid choice.")
            choice = input("Enter your choice: ")

        if choice == "1":
            if requests == []:
                print()
                print("No document requests have been recorded.")

            else:
                print()
                print("                 ✦ ALL DOCUMENT REQUESTS ✦")
                print("============================================================")

                request_number = 0

                for request in requests:
                    request_number = request_number + 1

                    print()
                    print("REQUEST", request_number)
                    print("------------------------------------------------------------")
                    print("Reference Number          :", request[0])
                    print("Requester                 :", request[2])
                    print("Property Owner            :", request[3])
                    print("Document Requested        :", request[4])
                    print("Tax Declaration Number    :", request[5])
                    print("Property Location         :", request[6])
                    print("Purpose                   :", request[7])
                    print("Request Status            :", request[8])
                    print("Staff Instructions        :", request[9])
                    print("------------------------------------------------------------")

                print()
                print("Total Requests:", request_number)
                print("============================================================")

        elif choice == "2":
            while True:
                reference_no = input(
                    "Enter reference number (or B to go back): "
                )

                if reference_no == "B" or reference_no == "b":
                    break

                found = False

                for request in requests:
                    if request[0] == reference_no:
                        print()
                        print("                  ✦ REQUEST DETAILS ✦")
                        print("============================================================")
                        print("Reference Number          :", request[0])
                        print("Requester                 :", request[2])
                        print("Property Owner            :", request[3])
                        print("Document Requested        :", request[4])
                        print("Tax Declaration Number    :", request[5])
                        print("Property Location         :", request[6])
                        print("Purpose                   :", request[7])
                        print("Request Status            :", request[8])
                        print("Staff Instructions        :", request[9])
                        print("============================================================")

                        found = True
                        break

                if found:
                    break

                print()
                print("Request not found. Please try again.")

        elif choice == "3":
            print()
            print("                ✦ FILTER REQUESTS BY STATUS ✦")
            print("============================================================")
            print("Available Statuses:")

            i = 0

            for status in statuses:
                print(i + 1, "-", status)
                i = i + 1

            status_number = input(
                "Enter status number (or B to go back): "
            )

            status_count = 0

            for status in statuses:
                status_count = status_count + 1

            valid_choice = False

            while valid_choice == False:
                if status_number == "B" or status_number == "b":
                    break

                if status_number.isdigit():
                    if int(status_number) >= 1 and int(status_number) <= status_count:
                        valid_choice = True

                if valid_choice == False:
                    print("Please enter a valid status number or B.")
                    status_number = input(
                        "Enter status number (or B to go back): "
                    )

            if status_number == "B" or status_number == "b":
                continue

            selected_status = statuses[int(status_number) - 1]

            print()
            print("Requests with Status:", selected_status)
            print("============================================================")

            found = False
            request_number = 0

            for request in requests:
                if request[8] == selected_status:
                    request_number = request_number + 1

                    print()
                    print("REQUEST", request_number)
                    print("------------------------------------------------------------")
                    print("Reference Number    :", request[0])
                    print("Requester           :", request[2])
                    print("Document Requested  :", request[4])
                    print("Property Location   :", request[6])
                    print("Request Status      :", request[8])
                    print("------------------------------------------------------------")

                    found = True

            if found == False:
                print("No requests found with this status.")

            print()
            print("============================================================")

        elif choice == "4":
            return

    
def update_status():
    print()
    print("                 ✦ UPDATE REQUEST STATUS ✦")
    print("------------------------------------------------------------")

    reference_no = input("Enter reference number (or B to go back): ")

    if reference_no == "B" or reference_no == "b":
        return

    found = False

    for request in requests:
        if request[0] == reference_no:
            found = True

            print()
            print("                 ✦ REQUEST DETAILS ✦")
            print("------------------------------------------------------------")
            print("Reference Number :", request[0])
            print("Requester        :", request[2])
            print("Property Owner   :", request[3])
            print("Document         :", request[4])
            print("Current Status   :", request[8])
            print("------------------------------------------------------------")

            if request[8] == "Submitted":
                print()
                print("[1] - Change to Under Review")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                while not (
                    choice == "1"
                    or choice == "2"
                    or choice == "3"
                ):
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Under Review"
                    print("Request status updated successfully.")
                    print("New Status:", request[8])

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

            elif request[8] == "Under Review":
                print()
                print("Use Verify Requirements to record")
                print("whether the requirements are complete.")
                print("------------------------------------------------------------")
                print("[1] - Go to Status Menu")
                print("[2] - Cancel")

                choice = input("Enter your choice: ")

                while not (choice == "1" or choice == "2"):
                    print("Invalid choice. Please enter 1 or 2.")
                    choice = input("Enter your choice: ")

                if choice == "1":
                    print("Please use Verify Requirements")
                    print("to update this request.")

                elif choice == "2":
                    print("Status update cancelled.")

            elif request[8] == "Action Required":
                print()
                print("The resident must address the instructions.")
                print("------------------------------------------------------------")
                print("[1] - Resume Review")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                while not (
                    choice == "1"
                    or choice == "2"
                    or choice == "3"
                ):
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    choice = input("Enter your choice: ")

                if choice == "1":
                    print("Please use Resume Request Review")
                    print("to record the resident's response.")

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

            elif request[8] == "Ready for Processing":
                print()
                print("[1] - Change to Ready for Release")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                while not (
                    choice == "1"
                    or choice == "2"
                    or choice == "3"
                ):
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Ready for Release"
                    print("Request status updated successfully.")
                    print("New Status:", request[8])

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

            elif request[8] == "Ready for Release":
                print()
                print("[1] - Confirm Document Released")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                while not (
                    choice == "1"
                    or choice == "2"
                    or choice == "3"
                ):
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Released"
                    print("Request status updated successfully.")
                    print("New Status:", request[8])

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

            elif request[8] == "Released":
                print()
                print("This document has already been released.")
                print("No further status changes are available.")

            break

    if found == False:
        print()
        print("Request not found.")

    print("------------------------------------------------------------")

def verify_requirements():
    print()
    print("   ✦ VERIFY REQUIREMENTS ✦")
    print("------------------------------")

    while True:
        reference_no = input(
            "Enter the resident's request reference number (or B to go back): "
        )

        if reference_no == "B" or reference_no == "b":
            return

        found = False

        for request in requests:
            if request[0] == reference_no:
                found = True
                break

        if found:
            break

        print("Request not found. Please enter a valid reference number.")

    print()
    print("Reference Number:", request[0])
    print("Requester:", request[2])
    print("Property Owner:", request[3])
    print("Document:", request[4])
    print("Current Status:", request[8])
    print("------------------------------")

    if request[8] == "Released":
        print("This request has already been released.")
        return

    if request[8] == "Ready for Release":
        print("This request is already ready for release.")
        return

    print()
    print("[1] - Requirements Complete")
    print("[2] - Requirements Incomplete")
    print("[3] - Cancel")
    print("------------------------------")

    choice = input("Enter your choice: ")

    while not (
        choice == "1"
        or choice == "2"
        or choice == "3"
    ):
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice: ")

    if choice == "1":
        request[8] = "Ready for Processing"
        request[9] = "Requirements verified as complete."

        for appointment in appointments:
            if appointment[0] == reference_no:
                if appointment[4] == "Booked":
                    appointment[4] = "Completed"

        print()
        print("Requirements marked as complete.")
        print("New Status:", request[8])
        print("Appointment Status: Completed")

    elif choice == "2":
        notes = input("Enter missing requirements or instructions: ")

        while notes.strip() == "":
            print("Please provide the missing requirements.")
            notes = input("Enter missing requirements or instructions: ")

        request[8] = "Action Required"
        request[9] = notes

        for appointment in appointments:
            if appointment[0] == reference_no:
                if appointment[4] == "Booked":
                    appointment[4] = "Completed"

        print()
        print("Request marked for further action.")
        print("Instructions:", request[9])
        print("Appointment Status: Completed")

    elif choice == "3":
        print("Verification cancelled.")

    print("------------------------------")

def resume_review():
    print()
    print("  ✦ RESUME REQUEST REVIEW ✦")
    print("------------------------------")

    while True:
        reference_no = input(
            "Enter request reference number (or B to go back): "
        )

        if reference_no == "B" or reference_no == "b":
            return

        found = False

        for request in requests:
            if request[0] == reference_no:
                found = True
                break

        if found:
            break

        print("Request not found. Please try again.")

    print()
    print("Reference Number:", request[0])
    print("Requester:", request[2])
    print("Property Owner:", request[3])
    print("Document:", request[4])
    print("Current Status:", request[8])

    if request[8] == "Action Required":
        print("Staff Instructions:", request[9])
        print()
        print("Check whether the resident has addressed")
        print("the missing requirements.")
        print()
        print("[1] - Requirements Now Complete")
        print("[2] - Requirements Still Incomplete")
        print("[3] - Cancel")
        print("------------------------------")

        choice = input("Enter your choice: ")

        while not (
            choice == "1"
            or choice == "2"
            or choice == "3"
        ):
            print("Invalid choice. Please enter 1, 2, or 3.")
            choice = input("Enter your choice: ")

        if choice == "1":
            request[8] = "Under Review"

            print()
            print("Request returned to Under Review.")
            print("Please use Verify Requirements")
            print("to complete the verification.")

        elif choice == "2":
            print()
            notes = input("Enter the remaining missing requirements: ")

            while notes.strip() == "":
                print("Please provide the missing requirements.")
                notes = input("Enter the remaining missing requirements: ")

            request[8] = "Action Required"
            request[9] = notes

            print("Request remains Action Required.")
            print("Updated Instructions:", request[9])

        elif choice == "3":
            print("Review cancelled. No changes were made.")

    else:
        print()
        print("Only requests marked Action Required")
        print("can be resumed.")

    print("------------------------------")

def staff_login():
    print()
    print("      ✦ STAFF LOGIN ✦")
    print("------------------------------")

    username = input("Username: ")
    password = input("Password: ")

    while username == "" or password == "":
        print("Username and password cannot be empty.")
        print()
        username = input("Username: ")
        password = input("Password: ")

    if username == "admin" and password == "123":
        print()
        print("Login successful.")
        return True

    else:
        print()
        print("Invalid username or password.")
        return False

def create_account():
    print()
    print("     ✦ CREATE ACCOUNT ✦")
    print("------------------------------")

    name = input("Enter your full name (or B to go back): ")

    while name.strip() == "":
        print("Please enter your full name.")
        name = input("Enter your full name (or B to go back): ")

        if name == "B" or name == "b":
            return

    if name == "B" or name == "b":
        return

    username = input("Create a username (or B to go back): ")

    while username.strip() == "":
        print("Please enter a username.")
        username = input("Create a username (or B to go back): ")

        if username == "B" or username == "b":
            return

    if username == "B" or username == "b":
        return

    for account in resident_accounts:
        if account[0] == username:
            print("That username is already taken.")
            return

    password = input("Create a password (or B to go back): ")

    if password == "B" or password == "b":
        return

    while password.strip() == "":
        print("Please enter a password.")
        password = input("Create a password (or B to go back): ")

        if password == "B" or password == "b":
            return

    account = [username, password, name]
    resident_accounts.append(account)

    print()
    print("Your account has been created successfully.")
    print("You can now log in using your username and password.")
    print("------------------------------")

def resident_login():
    print()
    print("     ✦ RESIDENT LOGIN ✦")
    print("------------------------------")

    while True:
        username = input("Enter your username (or B to go back): ")

        if username == "B" or username == "b":
            return ""

        if username == "":
            print("Please enter your username to continue.")
        else:
            break

    while True:
        password = input("Enter your password: ")

        if password == "":
            print("Please enter your password to continue.")
        else:
            break

    for account in resident_accounts:
        if account[0] == username:
            if account[1] == password:
                print()
                print("Login successful! Welcome,", account[2])
                return username

def resident_login():
    print()
    print("     ✦ RESIDENT LOGIN ✦")
    print("------------------------------")

    while True:
        username = input("Enter your username (or B to go back): ")

        if username == "B" or username == "b":
            return ""

        if username == "":
            print("Please enter your username to continue.")
        else:
            break

    while True:
        password = input("Enter your password: ")

        if password == "":
            print("Please enter your password to continue.")
        else:
            break

    for account in resident_accounts:
        if account[0] == username:
            if account[1] == password:
                print()
                print("Login successful! Welcome,", account[2])
                return username

    print()
    print("Login failed. Invalid username or password.")
    return ""

def my_requests(username):
    print()
    print("                      ✦ MY REQUESTS ✦")
    print("============================================================")

    total_requests = 0

    for request in requests:
        if request[1] == username:
            total_requests += 1

            print()
            print("REQUEST", total_requests)
            print("------------------------------------------------------------")
            print("Reference Number  :", request[0])
            print("Document Requested:", request[4])
            print("Property Owner    :", request[3])
            print("Request Status    :", request[8])
            print("------------------------------------------------------------")

    if total_requests == 0:
        print()
        print("You have no document requests yet.")

    print()
    print("============================================================")
    print("Total Requests:", total_requests)
    print("============================================================")

    if total_requests > 0:
        print()
        print("To view more details, select Track Request Status.")

def resident_dashboard(username, request_number):
    while True:
        print()
        print("        ✦ RESIDENT DASHBOARD ✦")
        print("--------------------------------------")
        print("[1] - Submit Document Request")
        print("[2] - My Requests and Appointments")
        print("[3] - View Available Documents")
        print("[4] - Book an Appointment")
        print("[5] - Cancel Appointment")
        print("[6] - Log Out")
        print("--------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            request_number = record_request(request_number, username)

        elif choice == "2":
            my_requests_and_appointments(username)

        elif choice == "3":
            show_available_documents()

        elif choice == "4":
            book_appointment(username)

        elif choice == "5":
            cancel_appointment(username)

        elif choice == "6":
            print("You have logged out.")
            return request_number

        else:
            print("Please enter a valid choice.")

def resident_menu(request_number):
    while True:
        print()
        print("     ✦ RESIDENT PORTAL ✦")
        print("------------------------------")
        print("[1] - Log In")
        print("[2] - Create Account")
        print("[3] - Back")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = resident_login()

            if username == "":
                pass
            else:
                request_number = resident_dashboard(username, request_number)

        elif choice == "2":
            create_account()

        elif choice == "3":
            return request_number

        else:
            print("Please enter a valid choice.")
        
def staff_menu(request_number):
    while True:
        print()
        print("       ✦ STAFF MENU ✦")
        print("------------------------------")
        print("[1] - Request Monitoring")
        print("[2] - Verify Requirements")
        print("[3] - Resume Request Review")
        print("[4] - Update Request Status")
        print("[5] - Logout")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            request_monitoring()

        elif choice == "2":
            verify_requirements()

        elif choice == "3":
            resume_review()

        elif choice == "4":
            update_status()

        elif choice == "5":
            return request_number

        else:
            print("Please enter a valid choice.")

def main_menu(request_number):
    while True:
        print()
        print("✦ MUNICIPAL ASSESSOR'S OFFICE ✦")
        print("--------------------------------")
        print("[1] - Resident")
        print("[2] - Staff")
        print("[3] - Exit")
        print("--------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            request_number = resident_menu(request_number)

        elif choice == "2":
            if staff_login():
                request_number = staff_menu(request_number)

        elif choice == "3":
            print()
            print("Thank you for using the system.")
            break

        else:
            print("Please enter a valid choice.")

main_menu(request_number)
    