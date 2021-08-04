from init_dc import client
import pathlib


class VideoStream:

    @client.event
    async def on_message(message):
        content = message.content
        channel = message.channel
        sender = message.author
        # Eloszor azt nezzuk meg, hogy a megfelelo joggal rendelkezo felhasznalo kuldte-e az uzenetet.
        # Es hogy az uzenet privat csatornan erkezett-e.
        if sender.roles.contains("Vetito") and channel.type == 'private':
            # Most nezzuk meg, hogy az uzenet megfelelo formatumu-e.
            # kezdodjon '!play' legyen kozepen egy space, majd a file-hoz vezeto eleresi utvonal.
            if " " in content and content.split(' ')[0] == "!play" and pathlib.is_file(content.split(' ')[1]):
                # Itt meg lehet a file formatumat valahogy validalni kene, eddig csak a letezest neztem meg ezzel a feltetellel.
                # A lejatszas elott megkene nezni, hogy van-e folyamatban eppen masik vetites. (Ez majd kesobb kene, de problemat jelenthet majd.)
                # csoda_mozi_vetito_fv(content.split(' ')[1])
                message.answer("Most kellene majd elindulni a filmnek.")
            # Egyebkent legyen ra valami valasz. (Lehet ettol valamivel specifikusabb kene???)
            else:
                message.answer("Az uzenet nem megfelelo formatumu.")