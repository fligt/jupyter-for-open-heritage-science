####### IMPORT PACKAGES #######

import matplotlib.pyplot as plt
import numpy as np

import ipywidgets as wg
from ipywidgets import Layout, Button, Box
from IPython.display import display, clear_output


####### DEFINE GENERAL PARAMETERS #######

style = {"description_width": "initial"}



####### THE FUNCTIONS #######


def overview():
    """Function that enables the selection and the visualization of various analyses.
    
    Args:
        

    Returns:
        It returns a python widget window in order to select and visualize the results of multiple analyses.
    """

    techniques_list = ['All','FTIR','MFT','Raman','RS']
    fake_projects_list = ['All','2022-015','2022-122','2023-003','2023-004','2023-005','2023-006']
    dates_list = ['All'] + list(np.arange(2015,2024,1))
    object_ids_list = ['All', 'PO060-A', 'PO068-A','PO068-D', 'etc.']
    
    wg_techniques = wg.SelectMultiple(options=techniques_list, value=['All'], rows=5, description='Analytical techniques', style=style)
    wg_projects = wg.SelectMultiple(options=fake_projects_list, value=['All'], rows=5, description='Project Ids', style=style)
    wg_dates = wg.SelectMultiple(options=dates_list, value=['All'], rows=5, description='Project dates', style=style)
    wg_objects = wg.SelectMultiple(options=object_ids_list, value=['All'], rows=5, description='Object Ids', style=style)
    wg_search_button = wg.Button(description='Search')
    output_button = wg.Output()

    params = wg.VBox([wg.HBox([wg_techniques,wg_projects,wg_dates, wg_objects]), wg_search_button,output_button])

    
    output_MFT_SP = wg.Output()
    output_MFT_dE = wg.Output()
    output_MFT_Lab = wg.Output()
    output_MFT_CIELAB = wg.Output()
    
    output_RS_SP = wg.Output()
    output_RS_SP_plot = wg.Output()
    output_RS_CIELAB = wg.Output()
    output_RS_CIELAB_plot = wg.Output()
    output_RS_fname = wg.Output()

    tabs_MFT = wg.Tab(children=[output_MFT_SP,output_MFT_dE,output_MFT_Lab,output_MFT_CIELAB])
    tabs_RS = wg.Tab(children=[output_RS_SP,output_RS_CIELAB])

    tabs_MFT.set_title(0, 'SP')
    tabs_MFT.set_title(1, 'dE')
    tabs_MFT.set_title(2, 'Lab')
    tabs_MFT.set_title(3, 'CIELAB')
   
    tabs_RS.set_title(0, 'SP')
    tabs_RS.set_title(1, 'CIELAB')
    
    
    
    output_FTIR = wg.Output()
    output_MFT = wg.Output()
    output_Raman = wg.Output()
    output_RS = wg.Output()
    
       
    
  

    def search_button(b):

        with output_button:

            clear_output()

            dic_params = {
                'techniques':wg_techniques.value,
                'projects':wg_projects.value,
                'dates':wg_projects.value,
                'objects':wg_objects.value}

            fnames_list = ['y.1000', 'y.2000', 'y.2010', 'y.2011', 'y.2123', 'y.2030']
            

            boxes = {f: wg.Checkbox(value=False, description=f) for f in fnames_list}
            

            techniques = dic_params['techniques']
            if list(techniques) == ['All']:
                techniques = techniques_list[1:]
            

            dict_tabs = {
                tuple(['All']): [output_FTIR,tabs_MFT,output_Raman,tabs_RS],
                tuple(['FTIR']): [output_FTIR],
                tuple(['MFT']): [tabs_MFT],
                tuple(['Raman']): [output_Raman],
                tuple(['RS']): [tabs_RS],
                tuple(['FTIR','MFT']): [output_FTIR,tabs_MFT],
                tuple(['MFT','RS']): [tabs_MFT,tabs_RS],
                tuple(['MFT','Raman','RS']): [tabs_MFT,output_Raman,tabs_RS],
                tuple(['FTIR','MFT','RS']): [output_FTIR,tabs_MFT,tabs_RS],
                tuple(['FTIR','MFT','Raman','RS']): [output_FTIR,tabs_MFT,output_Raman,tabs_RS]}

            list_tabs = dict_tabs[tuple(list(techniques))]       
            

            tabs_techniques = wg.Tab(children=list_tabs)

            

            if len(techniques) == 1:
                tabs_techniques.set_title(0,list(techniques)[0])

            if len(techniques) == 2:
                tabs_techniques.set_title(0,list(techniques)[0])
                tabs_techniques.set_title(1,list(techniques)[1])

            if len(techniques) == 3:
                tabs_techniques.set_title(0,list(techniques)[0])
                tabs_techniques.set_title(1,list(techniques)[1])
                tabs_techniques.set_title(2,list(techniques)[2])

            if len(techniques) == 4:
                tabs_techniques.set_title(0,list(techniques)[0])
                tabs_techniques.set_title(1,list(techniques)[1])
                tabs_techniques.set_title(2,list(techniques)[2])
                tabs_techniques.set_title(3,list(techniques)[3])

            
            with output_MFT_SP:
                clear_output()
                print('plot MFT data')
                

                


            
            with output_RS_fname:
                clear_output()
                @wg.interact(**boxes)
                
                def update(**kwargs):
                    clear_output()
                    for f in fnames_list:
                        clear_output()
                                       
            
               


            with output_RS_SP_plot:               
            
                fig, ax = plt.subplots(1,1, figsize = (15,10))                
                fs = 24

                
                for file in fnames_list:
                    clear_output()
                    Id = file

                    wl = np.arange(400,800,50)
                    sp1 = np.abs(np.cos(wl))
                    sp2 = np.abs(np.sin(wl))              

                    ax.plot(wl,sp1)
                    ax.plot(wl,sp2)


                ax.set_xlabel('Wavelength $\lambda (nm)$', fontsize=fs)
                ax.set_ylabel('Reflectance factor', fontsize=fs)

                ax.xaxis.set_tick_params(labelsize=fs)
                ax.yaxis.set_tick_params(labelsize=fs)                

                plt.tight_layout()
                plt.show()

         
            with output_RS_CIELAB_plot:
                
                fig, ax = plt.subplots(2,2, figsize=(10, 10), gridspec_kw=dict(width_ratios=[1, 2], height_ratios=[2, 1]))                
                fs = 20

                Lb = ax[0,0]
                ab = ax[0,1]
                AB = ax[1,0]
                aL = ax[1,1]

                Lb.set_xlabel("CIE $L^*$", fontsize=fs)
                Lb.set_ylabel("CIE $b^*$", fontsize=fs)
                AB.set_xlabel("CIE $a^*$", fontsize=fs)
                AB.set_ylabel("CIE $b^*$", fontsize=fs)
                aL.set_xlabel("CIE $a^*$", fontsize=fs)
                aL.set_ylabel("CIE $L^*$", fontsize=fs) 

                

                for file in fnames_list[0]:
                    clear_output()

                    L1,a1,b1 = 40,15,50
                    L2,a2,b2 = 50,18,30

                    Lb.scatter(L1,b1,marker='x', color='blue')
                    ab.scatter(a1,b1,marker='x', color='blue')
                    aL.scatter(a1,L1,marker='x', color='blue')

                    Lb.scatter(L2,b2,marker='o', color='green')
                    ab.scatter(a2,b2,marker='o', color='green')
                    aL.scatter(a2,L2,marker='o', color='green')


                plt.tight_layout()
                plt.show()    
                
                           

            with output_RS_SP:
                clear_output()
                display(wg.HBox([output_RS_SP_plot,output_RS_fname]))

            with output_RS_CIELAB:
                clear_output()
                display(wg.HBox([output_RS_CIELAB_plot,output_RS_fname]))
                
            display(tabs_techniques)

        
    wg_search_button.on_click(search_button)

    display(wg.VBox([params]))





