from django.contrib import admin
from restaurant.models import Payment,Meal,Booking

# Register your models here
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name','price','available')
    search_fields = ['name']
    list_filter = ['available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer','date','time', 'status', 'guests')
    list_filter = ['status','date']
    search_fields = ['customer__username','notes']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','amount','status','created_at']