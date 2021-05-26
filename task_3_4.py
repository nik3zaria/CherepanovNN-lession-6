from itertools import zip_longest


def users_and_their_hobbies(name_hobby_file, name_users_file, destination_file):
    with open(name_hobby_file, 'r', encoding='utf-8') as hobby_file, \
         open(name_users_file, 'r', encoding='utf-8') as users_file, \
         open(destination_file, 'a', encoding='utf-8') as writing_to_a_file:
        archiving_lists = zip_longest(hobby_file, users_file)
        for users_name, hobby in archiving_lists:
            if users_name is not None:
                users_name = users_name.strip()
                if hobby is not None:
                    hobby = hobby.strip()
                writing_to_a_file.write(f'{users_name}: {hobby}\n')
            else:
                quit()


users_and_their_hobbies('users.cvs', 'hobby.cvs', 'destination_file.cvs')