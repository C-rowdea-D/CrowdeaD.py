month = {
 "Jan" : "january" ,
 "Feb" : "February" ,
 "Mar" : "March" ,
 "Apr" : "April" ,
 "May" : "May" ,
 "Jun" : "June" ,
 "Jul" : "July" ,
 "Aug" : "August" ,
 "Sep" : "September" ,
 "Oct" : "October" ,
 "Nov" : "November" ,
 "Dec" : "December" ,
}
print(month["Jan"])
print(month.get("Dec"))
print(month.get("Luv", "Love"))
