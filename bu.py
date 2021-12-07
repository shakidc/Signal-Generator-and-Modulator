                #if i == 0: #signal initiator
                #    for j in range(0,len(t)):
                #        dmP.append(a*sin(2*pi*fc0*t[j]))
                #else:
                #    if d[i] == d[i-1]: #checking if the current data have the same value with the previous one  
                #        if dmP[-1] == a*sin(2*pi*fc0*t[-1]): #checking the last data from modulated data list
                #            for j in range(0,len(t)):                #and generate a signal with the same phase
                #                dmP.append(a*sin(2*pi*fc0*t[j]))
                #        else:
                #            for j in range(0,len(t)):
                #                dmP.append(a*sin(2*pi*fc0*t[-(j+1)]))    
                #    if d[i] != d[i-1]:
                #        if dmP[-1] == a*sin(2*pi*fc0*t[-1]): #checking the last data from modulated data list
                #            for j in range(0,len(t)):                #and generate a signal with the different phase
                #                dmP.append(a*sin(2*pi*fc0*t[-(j+1)]))
                #        else:
                #            for j in range(0,len(t)):
                #                dmP.append(a*sin(2*pi*fc0*t[j]))