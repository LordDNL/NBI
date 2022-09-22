class CDA:
    def __init__(self):
        self.landlords = {}

    def register_landLord(self, name, mobile, password):
        self.land_id  = f'00{len(self.landlords) + 1}'
        self.landlords[self.land_id] = {'Name': name, 'Mobile': mobile, 'Password': password, 'Tenant': {}}
        return self.land_id

    def login_landlord(self, land_id, passw):
        if self.land_id in self.landlords and self.landlords[land_id]['Password'] == passw:
            return {'msg': 'Successful', 'info':self.landlords[self.land_id]}
        else:
            return {'msg': 'Invalid Login credentials'}


    def register_tenant(self, NAME, MOBILE):
        import random
        tenant_id= f'{self.land_id}/{random.randint(300, 1000)}'
        self.landlords[self.land_id]['Tenant'][tenant_id ]= {'name': NAME, 'mobile':MOBILE}
        return tenant_id
