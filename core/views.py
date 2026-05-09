from django.shortcuts import render

def home(request):

    recommendation = ""

    if request.method == "POST":

        mood = request.POST['mood']

        if mood == "Happy":
            recommendation = "Pizza + Pop Music"

        elif mood == "Sad":
            recommendation = "Chocolate + Relaxing Music"

        elif mood == "Focused":
            recommendation = "Coffee + Lo-fi Beats"

        elif mood == "Tired":
            recommendation = "Energy Drink + Sandwich"

        elif mood == "Stressed":
            recommendation = "Green Tea + Meditation"

    return render(
        request,
        'home.html',
        {'recommendation': recommendation}
    )