from django.shortcuts import render

# Create your views here.
def dynamic_table(request):
    
    data = []
    steps = 255 / 49
    for i in range(50):
        val = int(i * steps)
        row = {
            'black': f"rgb({val}, {val}, {val})",
            'red': f"rgb({val}, 0, 0)",
            'blue': f"rgb(0, 0, {val})",
            'green': f"rgb(0, {val}, 0)",
        }
        data.append(row)
    context = {
        'rows': data
    }
    return render(request, 'ex03/table.html', context)