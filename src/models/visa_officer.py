import random

class VisaOfficer:
    def __init__(self):
        self.male_images = ['male.png', 'male1.png', 'male2.png']
        self.female_images = ['female.png', 'female1.png', 'female2.png']
        self.male_names = ['John Smith', 'Michael Brown', 'David Wilson']
        self.female_names = ['Emma Johnson', 'Sarah Davis', 'Lisa Taylor']

    def generate_applicant(self):
        counter = random.randint(1, 50)
        gender = random.choice(['male', 'female'])
        
        if gender == 'male':
            image = random.choice(self.male_images)
            name = random.choice(self.male_names)
        else:
            image = random.choice(self.female_images)
            name = random.choice(self.female_names)
            
        return {
            'counter': counter,
            'image': image,
            'name': name,
            'gender': gender  # Added for voice selection
        }