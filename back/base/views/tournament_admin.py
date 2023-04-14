from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage

from ..models import Tournament, Logos, WeightCategory, Sponsors
from ..forms import TournamentForm, WeightCategoryForm
from ..services import get_tournaments


@csrf_exempt
@login_required(login_url='base:login')
def tournamets_admin_update_info(request, slug):
   page_type = 'tournament_panel_update_info'
   
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      tournament_form = TournamentForm(instance=tournire)
      
      weight_categories_all = WeightCategory.objects.all()
      tournire_weight_categories = tournire.weight_categories.all()

      # Categories choosed for show
      weight_categories_selected = []
      weight_categories_unselected = []
      
      # Sorted weight categories
      for weight_category in weight_categories_all:
         if weight_category in tournire_weight_categories:
            weight_categories_selected.append(weight_category)
         else:
            weight_categories_unselected.append(weight_category)
          
      # get data from form        
      if request.method == 'POST':
         tournament_form = TournamentForm(request.POST, instance=tournire)
         
         if tournament_form.is_valid():            
            article = tournament_form.save(commit=False) 
                
            logotips = request.FILES.getlist('files')
            sponsors_logotips = request.FILES.getlist('sponsors-logotips')
            
            delete_logotips = request.POST.getlist('delete-logotips')
            delete_sponsors = request.POST.getlist('delete-sponsors')
            
            weight_categories_chooised_for_upload = [int(i) for i in request.POST.getlist('weight-categories-chooised-for-upload')]
            weight_categories_chooised_for_delete = [int(i) for i in request.POST.getlist('weight-categories-chooised-for-delete')]
            
            # upload weight categories chooised
            if len(weight_categories_chooised_for_upload) > 0:
               for weight_category in weight_categories_chooised_for_upload:
                  article.weight_categories.add(weight_category)
            
            # remove weight categories chooised
            if len(weight_categories_chooised_for_delete) > 0:
               for weight_category in weight_categories_chooised_for_delete:
                  article.weight_categories.remove(weight_category)
 
           
            # # delete choices logtips
            if (len(delete_logotips) > 0):
               for logotip in delete_logotips:
                  article.logos.filter(id=int(logotip)).delete()
                  
            # # delete choices logtips
            if (len(delete_sponsors) > 0):
               for sponsor in delete_sponsors:
                  article.logos.filter(id=int(sponsor)).delete()
         
            # # Add Logotips and Photos
            if len(logotips) > 0:
               for logo in logotips:
                  new_file = Logos(image = logo)
                  
                  new_file.save()  
                  tournire.logos.add(new_file)
               
            # # # Add Sponsor Emblems
            if len(sponsors_logotips) > 0:
               for logo in sponsors_logotips:
                  new_file = Sponsors(image = logo)
                  
                  new_file.save()
                  tournire.sponsors.add(new_file)
            
            article.save()
            return redirect('base:show_tournaments')
         
      context = {
         'page_type': page_type,
         
         'tournire': tournire,
         'tournament_form': tournament_form,
         
         'weight_categories_selected': weight_categories_selected,
         'weight_categories_unselected': weight_categories_unselected
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html', context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')
   
@login_required(login_url='base:login')
def tournamets_admin_delete(request, slug):
   page_type = 'tournamets_admin_delete'
   
   if (request.user.profile.userType == 'Админ' or request.user.profile.userType == 'Секретарь'):
      tournire = get_object_or_404(Tournament, slug=slug)
      
      if request.method == 'POST': 
           
         tournire.delete()
         return redirect('base:show_tournaments')
      
      context = {
         'tournire': tournire,
         'page_type': page_type,
      }
      return render(request, 'base/tournaments/panel/tournament_panel.html',context)
   else:
      messages.error(request, "You don't have permission to create tournament ;)")
      return redirect('base:show_tournaments')