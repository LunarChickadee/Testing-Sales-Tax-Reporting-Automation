Global county_list_NY

county_list_NY = "Albany,Allegany,Broome,Cattaraugus,Cayuga,Chemung,Chautauqua,Chenango,Clinton,Columbia,Cortland,Delaware,Dutchess,Erie,Essex,Franklin,Fulton,Genesee,Greene,Hamilton,Herkimer,Jefferson,Lewis,Livingston,Madison,Monroe,Montgomery,Nassau,Niagara,Oneida,Onondaga,Ontario,Orange,Orleans,Oswego,Otsego,Putnam,Rensselaer,Rockland,St. Lawrence,Saratoga,Schenectady,Schoharie,Schuyler,Seneca,Steuben,Suffolk,Sullivan,Tioga,Tompkins,Ulster,Warren,Washington,Wayne,Westchester,Wyoming,Yates,New York City/State Combined Tax"
selectall
removeallsummaries

field State

groupup

propagateup

field County

groupup

field State

propagateup

field "Gross Sales"

global total_total

total_total = 0

firstrecord



loop
    total
    right
until info("stopped")

firstrecord

loop

togglesummarylevel

downrecord

until info("stopped")

removeallsummaries

field State
propagateup

select length(County) > 2

removeunselected


local NY_City_Total 

NY_City_Total = 0

select State = "NY"

addrecord

County = "New York City/State Combined Tax"

firstrecord


loop

if county_list_NY notcontains «County»
    debug
    NY_City_Total = TaxableSales + NY_City_Total
    
// displaydata NY_City_Total
else
        endif
    
    downrecord
    
until info("stopped")
     
      
 lastrecord
 
 //displaydata NY_City_Total
  
 

 «Gross Sales» = 0
 field TaxableSales
TaxableSales = NY_City_Total
 
ExemptSales = 0
TaxableShipping = 0
ExemptShipping = 0

State = "NY"


firstrecord

debug

loop

    if county_list_NY notcontains County
        deleterecord
     endif
     downrecord
until info("stopped")

selectall
 
 
 


