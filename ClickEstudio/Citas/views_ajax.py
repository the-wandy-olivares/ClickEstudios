from . import models 
from django.http import JsonResponse
from .Options import Options
def Sale_Delete(request):
      sale_delete = models.Sale.objects.get(id=request.GET.get('sale_id'))
      sale_delete.delete()
      return JsonResponse(list(),  safe=False)



def DeleteService(request):
      s = models.ServiceImage.objects.get(id=request.GET.get('s_id'))
      s.delete()
      return JsonResponse(list(),  safe=False)

def DeleteMomentImage(request):
      m = models.MomentImage.objects.get(id=request.GET.get('m_id'))
      m.delete()
      return JsonResponse(list(),  safe=False)


def DeledeteImgMoment(request):
      m = models.MomentRelatedImage.objects.get(id=request.GET.get('delete_img_moment_id'))
      print(m.id)
      m.delete()
      return JsonResponse(list(),  safe=False)



def DeletePlans(request):
      p = models.Plans.objects.get(id=request.GET.get('p_id'))
      p.delete()
      return JsonResponse(list(),  safe=False)


def CreateCaract(request):
      try:
            p = models.Plans.objects.get(id=request.GET.get('id'))
            cr = models.CaratPlanes.objects.create(plans=p, name=request.GET.get('input'))
            caract_list = []
            dick  =  {
                        'id': p.id,
                        'name': p.name
            }
                  
            return JsonResponse(dick,  safe=False)
      except models.Plans.DoesNotExist:
            pass
      return JsonResponse(caract_list,  safe=False)


def DeleteCaract(request):
      cr = models.CaratPlanes.objects.get(id=int(request.GET.get('id')),)
      cr.delete()
      return JsonResponse(list(),  safe=False)

def Reserver(request):
      sale = models.Sale.objects.get(id=request.GET.get('id'))

      if sale.reserver == False:
            sale.reserver = True
            sale.reserver_mount = int(request.GET.get('input'))
            sale.abonado =  sale.plan.price -  sale.reserver_mount 
            sale.save()
            Options.Guardar_Ingreso(sale,int(request.GET.get('input')), ' - Abono'  )     

      else:

            Options.Guardar_Ingreso(sale,int(request.GET.get('input')), ' - Abono' )  
            print('depuración')
            abonado =   sale.reserver_mount  + int(request.GET.get('input'))
            sale.reserver_mount = abonado
            sale.abonado =   sale.plan.price -  sale.reserver_mount
            sale.save()
      if sale.reserver_mount >=  sale.plan.price:
            
            sale.saled = True
            sale.save() 
      return JsonResponse(list(),  safe=False)

def SaleService(request):
      c = models.Customer.objects.get(id=request.GET.get('id'))
      print(c.id)

      if c.saled == False:
            c.saled = True
            c.saled_mount = c.plans.price
            c.save()
            print(c.id)
      return JsonResponse(list(),  safe=False)


def SaleCancel(request):
      c = models.Customer.objects.get(id=request.GET.get('id'))

      if c.reserve == True:
            c.reserve = False
            c.save()
      return JsonResponse(list(),  safe=False)



def Search(request):
      lista = []
      # sale =''
      for s in models.Customer.objects.all():
            dict_customer = { 
                        'id': s.id,
                        'name': s.name,
                        'name_search': s.name + ' ' + s.number + " " + s.email + " " + s.date_choice.strftime('%d/%m/%Y') + " " + s.date_time_choice.strftime('%H:%M') +' ' + models.Sale.objects.filter(cliente=s).last().plan.name,
                        'sale_d': models.Sale.objects.filter(cliente=s).last().cliente.date_choice.strftime('%d/%m/%Y'),
                        'sale_h': models.Sale.objects.filter(cliente=s).last().cliente.date_time_choice.strftime('%H:%M'),
            }

            # models.Sale.objects.get(cliente=s),
            # sale = 

            lista.append(dict_customer)
      return JsonResponse(lista,  safe=False)

def SearchingClient(request):
      sale = models.Customer.objects.get(id=int(request.GET.get('id')))
      # Obtener todos los planes asociados a ese cliente específico
      # Obtener todos los planes asociados a ese cliente específico

      dict_client = { 
            'id': cliente.id,
            'name': cliente.name, 
            'email': cliente.email,
            'number': cliente.number,
            'sale': id,
      }
      return JsonResponse(dict_client,  safe=False)         

def Adicionales(request):
      # Obtener el plan
      plan = models.Plans.objects.get(id=int(request.GET.get('id')))


# Get all additional features associated with the plan

      # Verificar si el plan tiene adicionales
      lista = []
      if plan.adicionales.exists():
            adicionales = models.Adicionales.objects.filter(plans=plan)
            for a in adicionales:
                  dict_client = { 
                        'description': a.description ,

                  }
                  lista.append(dict_client)

      # pln = models.Plans.objects.filter(id=int(request.GET.get('id')))

      return JsonResponse(lista,  safe=False)         

def CreateAdicionales(request):
      print(request.GET.get('id'))

      p = models.Plans.objects.get(id=request.GET.get('id'))
      adicional = models.Adicionales(plans=p, 
                  description=request.GET.get('input'))
      adicional.save()
      adicionales_list = []

      return JsonResponse(adicionales_list,  safe=False)    


def Create_P_Adicionales(request):

      p = models.Plans.objects.get(id=request.GET.get('id'))
      p.final_price = int(request.GET.get('input'))
      
      p.save()
      adicionales_list = []
      return JsonResponse(adicionales_list,  safe=False)    


def Terminar_Cita(request):
      sale = models.Sale.objects.get(id=request.GET.get('id'))
      sale.saled_confirm = True
      sale.save()


      Options.Guardar_Ingreso(sale,sale.price_total, ' - Saldado' )       
   
      
      return JsonResponse(list(),  safe=False)          

def AgregarOpcion(request):
      pack_options = models.PackOpciones.objects.get(id=int(request.GET.get('pack_options_id')))
      sale = models.Sale.objects.get(id=int(request.GET.get('saled_id')))
      options = models.Opciones(
            sale=sale,
            name = pack_options.name,
            preci = pack_options.preci,
            description = pack_options.description,
            )
      options.save()
      return JsonResponse(list(),  safe=False)

def DeleteOption(request):
      option = models.Opciones.objects.get(id=request.GET.get('option_id'))
      option.delete()
      return JsonResponse(list(), safe=False)


def DeletePaquetOption(request):
      option = models.PackOpciones.objects.get(id=request.GET.get('option_id'))
      option.delete()
      return JsonResponse(list(), safe=False)


def CreateOption(request):
      sale = models.Sale.objects.get(id=int(request.GET.get('saled_id')))
      options = models.Opciones(
            sale=sale,
            name = request.GET.get('name'),
            preci = int(request.GET.get('price')),
            description = request.GET.get('description'),
            )
      options.save()
      return JsonResponse(list(),  safe=False)