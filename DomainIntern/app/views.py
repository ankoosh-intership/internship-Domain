from django.shortcuts import render, redirect
from app.models import DomainsModel
from pywhoisxml.lookup import Lookup
import whois
import requests
import dns.resolver
# import pythonwhois


# Create your views here.
def showIndex(request):
    dd = DomainsModel.objects.values()
    return render(request, "design.html", {"data": dd})


def displayIndex(request):
        dd = DomainsModel.objects.all()
        if request.method == "POST":
            ff = request.FILES["f"]
            print(ff)
            text = ff.read()
            txt = text.split("\n".encode('utf-8'))
            # print(txt)
            l = len(txt)
            for x in range(l):
                res = txt[x].decode('utf-8')
                res2 = [txt[x].decode('utf-8')]
                # res = w.domain_name +"\n" w.creation_date
                # res3 = dns.resolver.query('facebook.com', 'A')
                # print(res3)
                comstring = res.replace("it", "com")
                # comres= comstring
                comstring1 = [comstring]
                eustring = res.replace("it", "eu")
                eustring1 = [eustring]
                netstring = res.replace("it", "net")
                netstring1 = [netstring]
                orgstring = res.replace("it", "org")
                orgstring1 = [orgstring]
                infostring = res.replace("it", "info")
                infostring1 = [infostring]
                bizstring = res.replace("it", "biz")
                bizstring1 = [bizstring]

                try:
                    for a in res2:
                        a2 = a.replace("\r","")
                        w = whois.whois(a2)
                        date = str(w.creation_date)
                        res= w.domain_name +" \n \n" + str(w.creation_date)
                except (whois.parser.PywhoisError):
                        print(" no match found so free domain")
                # try:
                #     for b in comstring1:
                #         b2 = b.replace("\r", "")
                #         print(b2)
                #         w = whois.whois(b2)
                #         print(type(w))
                #         print(w)
                #         comstring = w.domain_name + "\n"+ str(w.creation_date)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")


                #
                # try:
                #     for a in eustring1:
                #         a2 = a.replace("\r", "")
                #         print(a2)
                #         w = whois.whois(a2)
                #         print(w)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")


                # try:
                #     for a in netstring1:
                #         a2 = a.replace("\r", "")
                #         print(a2)
                #         w = whois.whois(a2)
                #         print(w)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")

                # try:
                #     for a in orgstring1:
                #         a2 = a.replace("\r", "")
                #         print(a2)
                #         w = whois.whois(a2)
                #         print(w)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")

                DomainsModel(it=res,com=comstring,eu=eustring,net=netstring,org=orgstring,info=infostring,biz=bizstring).save()
            return render(request, "design.html", {"data": dd, "date":date})
        else:
                return showIndex(request)



def deleteData(request):
    print("delete")
    dd = DomainsModel.objects.all()
    dd.delete()
    displayIndex(request)
    return render(request, "design.html", {"data": dd})
