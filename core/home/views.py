from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("""<h1>Hello, world. I am a Django server.</h1>
    #                     <p>Here is a <a href="success/">link</a> to a success page.</p>
    #                     <br>
    #                     """)

    peoples = [
        {'name': 'John', 'age': 23},
        {'name': 'Jane', 'age': 24},
        {'name': 'Joe', 'age': 16},
        {'name': 'Jill', 'age': 26},
        {'name': 'Jack', 'age': 17}
    ]

    text = """
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Distinctio voluptates natus atque culpa quisquam dolorem suscipit, delectus velit corporis deserunt saepe libero exercitationem eum placeat est! Debitis at cum quae harum vel eos quasi nobis sequi distinctio blanditiis, quos dolor. Velit deserunt quas tempore accusamus enim amet deleniti dolor molestiae asperiores magnam hic quibusdam, odio, pariatur officiis porro ducimus eius expedita reiciendis nisi vel rerum, atque minus? Eius deserunt repellat odio nemo inventore dicta itaque? Fugiat facilis illum culpa aliquam pariatur facere suscipit dolorem nostrum tempora, quasi soluta laboriosam. Quo doloremque explicabo sit distinctio quas, a exercitationem minus iusto? Dignissimos?
        """
    
    vegetables = ['Pumpkin', 'Tomato', 'potato']

    return render(request, 'index.html', context = {'peoples': peoples , 'text': text, 'vegetables': vegetables, 'page': 'home'})

def about(request):
    context = {'page': 'about'}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html', context = {'page': 'contact'})

def success_page(request):
    return render(request, 'success.html', context = {'page': 'success'})