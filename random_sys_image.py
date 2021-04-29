from discord import Embed

from command import Command

# Images of System Boys
custom_images = [
    'https://scontent.floh1-1.fna.fbcdn.net/v/t1.6435-9/83398931_2538985876423421_2627695716503388160_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=sxT918ZJp44AX94jg7S&_nc_ht=scontent.floh1-1.fna&oh=cae3836519615d85537b209d799aac78&oe=60B16A57',
    'https://scontent.floh1-1.fna.fbcdn.net/v/t1.18169-9/12548850_930165383725735_8884847447759217784_n.jpg?_nc_cat=104&ccb=1-3&_nc_sid=174925&_nc_ohc=G14Gb4hgcokAX_aan6I&_nc_ht=scontent.floh1-1.fna&oh=11301e27945f2bbcb570ea2ea72a85d5&oe=60B16D23'
]


class Random_Sys_Image(Command):

    def on_triggered(self):
        return Embed('Testing')
