
def adding2db(new_file_info,db):
    new_file_info = file_info(file_name = "file_name",folder_name = "playtest",email_id="rj@gmail.com")
    db.session.add(new_file_info)
    db.session.commit()