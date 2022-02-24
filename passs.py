print('Directory changes')
Password = input('Enter the password : ')
passkey='1'

if Password == passkey:
    print('1:enter a new contact ')
    print('2: delete a contact ')
    print('3:get directory : ')
    innp=int(input('1/2/3'))

    if innp==1:

        c=input('Name: ')
        b=(input('Contact: '))
        d=(input('Email ID: '))
        k=0

        f1=open('pass.txt','r')

        for line in f1:
            if c in line:
                k+=1
                print('name exists')
                break
            elif b in line:
                k+=1
                print('number exists')
                break
            elif d in line:
                k+=1
                print('mail exists')
                break
        f1.close

        if k==0:
            f1=open('pass.txt','a')
            f1.write('Name: ')
            f1.write(c)
            f1.write('\n')
            f1.write('Number: ')
            f1.write(b)
            f1.write('\n')
            f1.write('E-mail ID: ')
            f1.write(d)
            f1.write('\n')
            f1.write('\n')
            f1.close

        else:
            print('nothing was added')






    if innp==2:

        delet1 = input('enter the name to delete ')
        f1 = open('pass.txt','r')
        lin=0
        hoist=0

        for line in f1:
            lin+=1
            if delet1 in line:
                hoist = 1
                break

        if hoist == 0:
            print('Contact doesnt exist')

        else:
            f1 = open('pass.txt','r')
            rem = f1.readlines()
            f1.close

            del rem[lin-1:lin+2]
            new_file = open('pass.txt','w+')

            for line in rem:
                new_file.write(line)

            new_file.close
            print(delet1,'was succesfully deleted')






    if innp == 3:
        f1 = open('pass.txt','r')
        direc=f1.read()
        print(direc)




else:
    print('wrong password')
