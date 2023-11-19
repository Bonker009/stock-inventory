import base64

import qrcode
from django.shortcuts import render, get_object_or_404, redirect
from io import BytesIO

from .form import ProductForm
from .models import Product


def home(request):
    # Retrieve all products from the database
    products = Product.objects.all()

    qr_codes = []  # List to store the generated QR codes

    for product in products:
        # Generate the QR code for each product
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        url = request.build_absolute_uri(product.get_absolute_url())
        data = f"Product: {product.name}\nTotal Price: {product.total_price}\nURL: {url}"
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Create a byte stream to store the image
        stream = BytesIO()
        qr_image.save(stream, "PNG")
        stream.seek(0)

        # Convert the image data to a Base64-encoded string
        image_data = base64.b64encode(stream.getvalue()).decode("utf-8")

        qr_codes.append((product, image_data))  # Add the product and its corresponding QR code to the list

    context = {
        'qr_codes': qr_codes,
    }

    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'home')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
