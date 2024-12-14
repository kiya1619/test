from django.shortcuts import render
import pandas as pd
def home(request):
 

    csv_path = 'C:/Users/kiya/Desktop/kiya.csv'
    data = pd.read_csv(csv_path)
    data['Lastname'] = data['firstname'].apply(lambda x: 'Shibru' if 'abdisa' in str(x)
                                                else('geta' if 'tsegaye' in str(x)
                                                      else('kiyu' if 'kiya' in str(x)
                                                            else "")))
    data_list = data.to_dict(orient = 'records')

    count = data['firstname'].value_counts()
    data.to_csv('new_save.csv', index=False)
    print(data_list)
    context  = {
        'data_list':data_list,
        'count': count

    }


    return render(request, 'temp/home.html',context )