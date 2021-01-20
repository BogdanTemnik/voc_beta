import speech_recognition as sr

r = sr.Recognizer()

string = b"""\xff\xf3D\xc4\x00\x10\x80M\xf0\x01O\x18\x00\x90\x94\x02\x90\x01 \x02\x80 \x08a\x08.\x04,\x9d\x973M\x0fg\xbf\xbb\xc0\xc4\x10\x0c\x02\x00\x80cPc\xfe\x0f\xf2\x80\x87\xff\xeb\x07\xde\x8fX \xe0|>#\x07\xf1\x00>\x1f(\x18(\x18\xff\xf3\xff\x87\xe0\xf8>\x1f\x0b\x17HR\xc4(\x07k\x1fI\xb3\xc8\x80\xb8=\x7f\xcf\xff\xf3D\xc4\x11\x16\xeanl\x01\x94\x80\x00\x90\xc2!\xfe+A:\x1e\x0b\xa8\xff\xc6|d\xc8\xb8\xe7\x9f\xff\xf2\xba\x11\x90\x10\x8c@?\xff\xc1\xb6\xe2\xc6N\x07\xbe  \xb0\x07\xa9\xff\xff\x92\xa3\xbcX\xc3\xd0\x10`\n\x82\xfcd\xc7?\xff\xff\xfc\x89\xa8\xbe\xa6437/\x9fc\xff\xff\xca\x000\x02\rE\xd7\x9e}v?\xf5\xff\xf3D\xc4\x08\x13s\x12\xbc\x01\x878\x00\xfc\xe3M_\xf6O\xff\xa7\x1d\x1e\xf57\xd5\xd1\t\x8fW\xb2\xab\x0f\xbaX\xbc\n\xb3\x93.T\x89\x04[\xb9\xe4\xcc\x1fv\r\x84\x02 -\x19\x11\n0\xdd\xff\xfa!\xf2n\xb38\xb9\xc6\xae\xc2\x8b\xb1\xed\xff\xff\xf7\xbf\xfd\xdd\xd2:O\xa62\x11\x08\x01@\xe4\x05\xc3\xf1Cl\x1c\x08\xff\xf3D\xc4\r\x14z\x1e\xbc\x01\xc8@\x00\x0bw\xf9\xff\xff\xff\xff\xff\xff\xbf\xf8\xde}a7\xf9\xb8\x8d,z$W\xfd\x7f\xf2\xb5tQ\xa2\xbf\x03E\x05\xd6\xc5\x8a\x11\xc2\xa3Q\x85\x89\x82\x8f\x13J\xf0H\xaa\x8a\xaaC^\xd1\xc3\xa9(\x1e\x02\x82\xa2\x87\x8dZ\x8d^\xed\xaf\xd3\xb1\xfb\xc3\xd5H$1\xadW\x88\xc1\xa0\xa3\x0f\xff\xf3D\xc4\x0e\x15!\xd6\xb4\x00\xc2\xde\x98VVO\xb6\x10e\xce\xfe\x0b/\xfd\xcd\xfe\x95w\xcfH3\xe1\xe0~.\xda\xa0\xd8\xafe\xf6\xc4\xa9E\xac\xde\x1b\x00\xb6C{\xf3+\xfcb\xb9\xf0\xe7\xd5>\xef\xba\xd7_/\xed\xbc\xcbI\xab\xf7\xe9\xef|^X\xf0\x9e\xbe\xd9\xe3\xf6yU\x9d\xff\xd60\xd0\xfa\xe7\xac\xf3\xdb\xa9-\xff\xf3D\xc4\x0c\x15!\xce\xb8\x00\xc3X\x94\xc4\x9bP\xa6t\xb8\x02l=\xa6\xb7\x8f\x85\xdbi\x0f\xaf\xcc\xc7y\xfdg\t\x01ijE\x82t\xf7\xef\x8eQW,\xf9x=y\xc8=\xc0\x17\x13r\xbf\xcb/OWazw\xbbQ\x7f\xce@y\x95\x9c\xe6:\xb9m\xbb\xd93G\x19\xa5\xe1\x95\xdf\xf9\xb9\x03\x16\xec\xfaa\xe8\x94\xff\xf3D\xc4\n\x15\x11\xc2\xc0\x00{\xde\x94\xac\t\xa1\xe48Bn\xb7\xbb\xf24hV$L\xc0[\xc6\xbf_K\xcf]\xca\xd4\x99\x97\x1f\xa4\x08\xdc;g\x1d\xbd\xc79\xf5\x94\xd6\x8b;,j\x17\xa5S\xff\x07*mg\x19\xa4<\x7f\xedwY\xde\xf5g\rz^\xb0u\xfek%\xbe\xb7\xa8\x1a\x95V\x8a\xc9\x10](\xafa\xff\xf3D\xc4\x08\x11\x99\x96\xc4\x00k\xd0\x94\xe6\xff\x05\x84>\x0c\xaf=Z\xc1\xd8IQ\xb8\xbf\xa0\xf3\x8f\xeb\xd3"H\xf3\xfa7\x12i\xab\xae\x1d\x0b\t\xef\x9d\xc2\x89\xc1G\x86\x06\xafl\x1c\xbfiB\x19\xb7\xc4\r\xaa\xf9\xc4\xc9\xf4\x82\xf2\xff\x8b#\xa4\xb2*n\xa2\x00\x13\xee\x08?\xd2p\xfaFn\x96\x822\x82\x0e\xef0\xf1\xff\xf3D\xc4\x14\x10\xc1\xb6\xc0\x00;\xd4\x94\x91\xd9\x8d\xea\xba7\xca\xcdZ\xd8D\x8f\x08\xdf\xd4dg\x85u\xec#\x85;\xb5L\x08\xdd\xd5\x08\xc2\xf4\x9f\xb8\x823\xa9\x10\xfc\xfd\n\x8b\x1bX\xf2F\xf2G=\xce\x900\xad\xd6M\x8b\x13\xfc\x8d\x8627\x1f\n\xc5 \'\xa3\xc3\x89#\xc5,[j\xaf\r\xd3\x87\x1a\xb3\x1c\x046\xff\xf3D\xc4$\x12q\x9e\xbc\x00\x83\xce\x947\x86\xa5\x01\xe8\xc7(\x19 \xb9P~\x0f\x9d&\x04b\xd3)<L6\xd2P\x96\x8d8\x95.<I[*5g\xc0\xcd\xa2d\xd54\xa4\x10\x01\xad/\xf8,;\x94\x90\x80\\\x860\xa1\x00M\x15\xe4\xd4V\xb6\xefC0]6\t\xc3$&r\x97\x1dV\xa8\x8c\x81\xf7i\x12\xa8\xff\xf3D\xc4-\x11\xa9\x1e\xb4\x00zRq\xf9\xac\xc1\x99\n\x19i\xedNlF]\x10_\xcao\xca\x87\xd3.\xb9c\xef\xff\xaf\xd5,0#\xc5;\x83\x08\x9b."A\x89\x1a\xf6\xde\x9fF\xff4O9A\xd7\xb8\xef[\xc5X(\xf45\x1fl\xd4n\x1f6\xd9\xa8\xa6\x19Y\x10\xa9\xa2"h\x8aX|\'\x1bg\xc9N\x965\xff\xf3D\xc49\x119&\xa0\x01OH\x00\x02\xb0JT\x15\x15<\r\x1e=\xff\xd0F\x82\xe5\x88\x82,\xea)\xaa1\xff\x14T\xd1M\x0bMR\x1d8\xac\x05\x00Cu(\x80\x98\n\x84\xe6[\xfa\x84\x17@*\x0b\x0c\x1d\x1a]E\x05\x06\x17\x81,T ]\n\x14eEh\xd9F|\x8c\xa1Y\xc9F\xe0[\xc0.\xe1Y9\xff\xf3D\xc4G\x1d\xd9Jl\x01\x99H\x01\xeb\x89/\xcf\xedU\xaf\xe5\x1c\xad\x81\xee\x8cZ\xa5\xa7\x15\x94\x1bt\xcckZ\x8c:\x0cHC2-\xcb?[~\xbf\xf8\xdbY?\xef\xf7\xd9Z\x0b\x7f\xfa\x95\xbfU\xfb\x89\x88\xb3R\x1a<\xa3\xb9\xb2\xcf\xc9\xf7W\xb0K\xa8mX\xa5\xed\xa6 \xc8\x1d\xa6\xcb\x1c\xe5\xd6\xc6A\xa1\xa1\xff\xf3D\xc4"\x1a\x9aJ\xb8\x01\x8fX\x00q \xe1q2\xafa\x81~p\xbf\xc7`\xc8\xa0\x86\x1d\x04\xf7\x18\xb9\xa3a\x95\xff\xf9z\xc7\xe1\x93\x9ds\x0e&y\x7f\xff\xff?\xd3\xdb\x13.6dL\xfb\xbf\xff\xff\xdd+]M\xff\xe6\xb6\xd1\xc3\x8b\x7f\xe9\x01)\x8c\x01\xcd\x07\x80\x8cr\xc3\xca\x04GI\x94\xb3R8\xd7\x99\xbb\xff\xf3D\xc4\n\x11Y.\xb4\x01\xc8(\x00Z\xd3\xff\xf6\xfb\xfa\xdb\xecgT\xa9\xccr\xa8\x80x\\\x81\xd0\x98|\x04\x17\x08\x8a\x06\xab\x94y\x1aM\x02\x85P\x95\xb5\xecH\x80<8\x11\xa0\xe1\x13\xcd\xb4\xc2G\x07\xcci\xfe\xbcrX=U\xa1UN\xe9\xe1\x9a c\xd0\xdb\x0c\x95\x8b\x02\xe6\x00z\x02\xe1aI=\x13{\x8a\xff\xf3D\xc4\x17\x11\xa9&\xb0\x00z\x04p\xde_\xfd\xb6\xe9\xff\xa1\xd8\xc0\xe5e\x108f\x01\x81\tq\x83\x0f\x11\x1aAd\xf6V\xf0\x18<\t\x94@\xb70A\x0b\xab\xff\xf7s\x04\x00\xeb, <+R\x95w\xd7\xd8\x99[\\\x99\xfa\xd4\x8f4\xf5\x12/l\xd4]\xa4+\xcai\x80^+2z\xad\x8c\xeb"*K\xed\x06\xff\xf3D\xc4#\x15\xea\xba\xa8\x00\xc2\n\xb9\xcd\xa4\xfb\xc4E\x9fC\x07\xb1\x83\nmX\x1c\xb5@\xa1q\xaa\xa8\x8c\xb6\xaf\xf7\xca]J\xc84Q^\xbf\xeb9\xdf"\xe8\xb5o\xff\xff\xff\xe5\xd4\xaa\xea\xa4)\xc6\x8e7\x8f\xe5\x8b\xe1]\x0en\xaf\xca\x91\xd5\xa6\xd4\x15Y\x96\x81\x02\x80\x8b\x98\x153hQ=!\xc4[&\x19t\xff\xf3D\xc4\x1e\x14A\x92\xac\x00\xc2P\x94/.W\x1at\xb5\xbc\x92\xd3\xb4\xcb\x9c4\x80\x84\xe0\xf4H*\x82\x88;-\xe0\xdbkA\x91O\x1bM\xd7\xd7\xbcp\xbf\xdf\x04\\Y\xaf\x1c\xffs\xbf\xff\xff\xe8\x04Ek%\xea\x1d\x8f)\x8a\x93\xac\'\x90S\x12x\\b#\x87gr\'\xafZ\xbb\xaf])~\xb4\xa6\xe1Y\x14\xff\xf3D\xc4 \x12\xa9\xd6\xc0\x00\x82\x12\x99Z\xc8\x07\xc4b\x01\xa22F\x17\xc3i\x15( 2D$t\xe5\x0c\x96f\xfd\xcd\xcf\xe3\xbb\x90\xfb\x8f\xf8\x8e\xe6\x93\x1fa\xff\xff\xff\xed\xbf\x82\x8d\xfao}\xea[M\xe5\xf9\xfb\x00\r\x85\xea~\x11\xe7l\x99\xcb\xber\xd9\xe8B\xc8\x8btP\x05%\xa2\x9c\\T\xfaT\x89\xc8\x1e\xff\xf3D\xc4(\x10\x91\xa2\xc0\x00x\x92\x94)\x98\x80\xde]\xb39nz\xdfR\xab\xad\xf7\xbe4\xf9!Z\xa0\xf3\xd1I\xea\xee\x06\xaa\xa4\xb1\xb5\xd1\xca\xc9\xb8\xe7^}I\x8bU\xb2\x03\xc5\x02\x0f\x81\x1e7h\xebQ\xb6\xcez\xe8H\xec\x8c\xe1\xef\xd2\xaaw\x13\x15{\x1e\x83\xdej\xed#yh5\x064\xb5"\xb5\xa7\xf7\xe7\xff\xf3D\xc48\x12)\xa2\xac\x00\xc1\xd8\x94f\xd3\x9f==\xbdY\xda\xc6\xb7\x17|O\xb8\x14\xedEj\x18\xd01\xbd`2\te\xf6\x88\x978@\x07C\xce\x94\x08^\xa3\xda\xd0\xc5\xfb\xeby\xb41\x10\xc2Jr\t\x04\xc7\x80\xc7p\x15\x9co\x07\x1e@\xf8*\x08"C\xcfmy\xbf+Y\xdc,\x05T\x1a.y\xd4R\x10\xff\xf3D\xc4B\x11\xb1\x9a\xa4\x00\xc1\xca\x94G\xff\xff\xfc]\x1a\xbd\xf81\xa3=\x01\x9c\xfav)\x8b(\x81\x08\x00mEv6>\xec\xca\x99*l\x7fd+\x7f\xe5\x97\xeb\xbf\xe6\xcdd\x06\xe1l\xab\xf1\xd9\x1cS\x0f\x04P\x90\x8a\x8d\xa2W\x0b%\x97\\\x8a\x142|,\xf3\xda\x94\x85\xff\xff\xffL\xea\xd0yeO\xa9\x14r\xff\xf3D\xc4N\x11\xf9"\x9c\x00|\xd2p\x8c\x83\x02\xfd\xd3\xaf%\xec\xc3\xe0Y\x89n\x1c\xbf\xff\xff\xbc\x7fx\xcbn\xbf\xbc\xaf\xbe\xa3\x92\xbd\x99Q.\xac\x8a\x91M\xa4\xf2R\xb6i\x12D\xc3&\x1f\xc4A[\xaa\xde\xf2\x01[\x85@\xa4DA\xdd\x8b\x02\n\x9d\xff\xff\xff]z\x00KF\xa4\xff"\xd3RN\xe5\xa4\x97<\x87\xff\xf3D\xc4Y\x12i\x16\x90\x01XH\x00{\x02\xcb\xe6\xb2\xc7\x03SdZ\xd8\xfc\x9aJDv\xc5\xd4\xfd@z\x10\x02\x00w\x8d\x947$\xe8\xe1\xf2\xf5\x86\xf0\xc06&\xdf\xa4\x8dl\x9b\x7fnl9\x186\xff\xf9\xbeNl8R\x918\xe1,\xed\xa2M\xeaTc\xfdM\xe3\xa0|a\xa1\xc6\x0e\xc3\xd5W\x111\x0f\xad\x95\xff\xf3D\xc4b!s"\x84\x01\x98X\x01\x1f\x1f\xfeV;\xd8\x03\x81\xa0\x8a\x04fh,}\x7f\xf8\xae\xbf\xff\xfe\xbf\xff\xff\xf97Dw\x9f\x1f\xd4\xa4\xd78n\x9d\r9Hm\xf5\xff\xff\xff\xff\xfd]\xdf\xdb\xd9z\xf3E\xadM\xb2\xd6\x93uu\xaa\xc9\xe9"\xcc\x9a\x08\xa4\xa3\x86F\x0b\x97\x8d\x10M\x03Z,bJ\x1a\xa0\xff\xf3D\xc4/\x1eS"\xb0\x01\x87h\x01I(\xba;\xd27%\x1005b\xfb\x08\xa1\xd80\xc4\x13#\xe5\xc1b\x17\xb5\x18\x19\x91\x84\xc4&\xe5\xd1\x847.\x0fC\xe5\xf9}\x13gM4\x10M\x04\x10\xc7x\xc1\x8e\x03e\x1cMH\xa2cc\x1cOM\x06\xd2\x92D\xb9&K\x96 \xe4\xc9\x15\x14\x9f\xff\xff\xff\xff\xff\xff\xff\xf3D\xc4\x08\x13\xf3\x12\xc4\x01\xc2P\x00\xff\xff\xff\xff\xfe\xa9f\xa3-s\xdb\xf5W4\xd3\xd0\x90\xc50\xe9\xa6\x16C\x88\x84D,\t\x05F\xe6\x8b\x05X^J\xa3\x8c\xc4&\x13\x16\x10Dd\xc3\x10\x907 "\x8cK\x08\x865\xdc\x8c\x84\xe2\xf3\xfdg\xcf\'0\xfa\x97S\xc9I\xd9/\xff\xff\xff\xff\xff\xff\xff\xf7\xf1T\xff\xf3D\xc4\x0b\x14\xbb\x16\xc4\x00\x08\x10\xb9\xed\xe95\xd2/\xdc\xde\x8a\xf3=\xb8\xbc\xb4\x92\xe84 <\x1c\x1c\x1f\x0f\x0f\x82qad\x0b\x8c\x15\x1f\x02(\xe1\x18b\x85\xa4T\xd1a\x1c\xf7\x1a\x1f\x87b+\n\x0b\x12-n\x1e1\xa84^\xd5\xe4<\x93\x1d!\xca\x9ba\xc2!m\'6\x11\xff\xff\xff\xff\xff\xff\xff\xfc\x97\xff\xff\xf3D\xc4\x0b\x143\x0e\xc8\x00\x10P\xb9\xff\xff\xff\xff\xed\xff\xd57)\xcdli\xd1\xff\x1c\x94\xdfb+\x0c\x91\xa1[\x16$+:\x04!\xf8\xc2\xc4AaP\xa0r\xd0]\xb2\xe3L"\x823L\xc4\x11\x15\x99\x91hz\xf9\xf0\xca\xaee\xc9!\xc0\x9c\x95[\xa2\x9bf\x16\xe9b\x0f\xff\xff\xff\xff\xff\xff\xff\xfe\xbf\xff\xff\xff\xff\xf3D\xc4\r\x12"\xb2\xc0\x00\x08P\xb9\xff\xe6\xbf\xf8\xba\xe7\xe3\x92\xa4{\xff_k-s\x17\x058\x8c\x15\x12)\x81\xfd\x8b\x03P\xc8\xa0\xba8\xc9\x10\xa0TH\\S:\xcd\x9dLP\xb8\xad\x8c\xa4\x1ag\xdc96\xb8\xe3Q\x7f1\x15\x94Z\x03?\xfb7\xff\xff\xff\xfeBU\x91\x16\xfe\xa5\xa0q\xc6/_\xf7\xff\xf3\xdf\xff\xf3D\xc4\x17\x12\xa2v\xa8\x00\x10\x90\xb8\xff\xf5\x7f~\xcaH\xe8\x9aS\x96\x15W\xd5v\xbb\xeaXB<\x9cB<\x1a\x82\x91 \x9e\x8d(\xa7T\xb4jf[\x8b\x99$95\x8b\x98R\xc6>%\x8f\xbd+P4\x8a\x07\xfc\x0b\xde\xfb\x7f\x0e\x1d R%)\xf5\xbe\xc7=m\xf7\xd4\xd3|\xe3\x9a\x84\x8e\xad\xaa\xddM4l\xff\xf3D\xc4\x1f\x11\x822\x88\x00y\xc4\xb8\x0b\x87\xc6\xb7\xe9\xff7\xfe_Su\xa9h\xff\xd4\xa5\xd5\x91\xcc\xac`#\x97(\x90B\xa1R\xd2\xcfx,\xf2\xcfTK\xb3\xf3\xc98\xa3\x1d\x98\xa5\xddC/\xed$\x8a]*\x86\x81q\xc2\xc2\xcc\xcb\x0cqMu\x11l\xcc,\xc6|\x91\x8e\x1d6mW\xbc?\xf20l)\x81\xa7\xff\xf3D\xc4,\x10\xa9\nd\x00\xd2\x06p\xff\xf3I\xb2Z\xda\xe5\x03\x97B\x80\xaf\xab\xc3\xb0T\xeb\xf5\xedn\x90h\xdd?\xc9\x0c(\xf4\x8aV\xd8\xcb\xaa\xe5Q\xcf\xe3Iir\x13\xce|\x9d\x96\xd9\xdb\xbb\xed\x8c\x8d\xb3\x02\x82)\x19\x01j\xc3\x94oc-r\xc0\x85\x12Q5\xd4\xae\r=\xc0\x17(\x9c\xf5w\x01\x96r\xea\xff\xf3D\xc4<\x12i\n<\x00\xd1\x86pL+\x9c\\\x1a\xb5]_\xa7\xb9\x0f~H\x8a9aS]\x06G\xf89\xf9\x96\xbb3\x19H\x12N\x8dmv\xdd\xaa\xa4k\xb2\xaf\r\x82\xd0P:\x98\x86\x9eJ\x1c\x8b\xb8\xab\xf8o\xb1|]\xc8V\xa6\x92pu\xb6$\xadn\xa9\x04w\xb3\xb4Z\xd6i,\xf5;\x8b\xb9O\xe96\xff\xf3D\xc4E\x11\x00\xa6,\x00\xd9\x86L|\xe3\xaf@\x00\x02\xca\x9ak:\xbb\xba\x82WR\xf5\x99\xd2\xc3:\xe1\x85yT\xa1\x9c\x15:NU\xd2"/\x11\x1e\x96*\xb0T$\xf0\xe9/-\xc4\xae\x11T\x05;\xd4t\xab\xa2`3\xfc\xaa\xa4yo\xe2*LAME3.100\xaa\xaa\xaa\xaa\xaaLAME3.\xff\xf3D\xc4T\x0f\xe0\xa2\x00\x00\xd8\xc4L100\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaaLAME3.\xff\xf3D\xc4g\x00\x00\x03H\x00\x00\x00\x00100\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaaLAME3.\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00100\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa', 'src': b'\xff\xf3D\xc4\x00\x10\xb81\xf4\x01O\x00\x00p7\xc1\xb6\x01\xb8\x07a\x86q\xd9\xe3;\xf8\xe2\x03\x82pA\xd8&\x0f\x9f\xfcH\x18X>8\x1f\x0f\xe0\x98>\x0f\xf1\x03\xbe \x07\xc1\xf3\xf0p\x10\x83\xe0\xf8!\xc4\x87?\x94\x04\x03\x1f\x97\x7f\xc1\xf0|\x1cw\xf2\x80\x80 f\xee\xe1\x91\x8a\xe6\xff\\\x98T0r\x86\\l8\xff\xf3D\xc4\x10\x15A\x1el\x01\x9c\x98\x00\x06b\xa2\xa1\x93\x0f\xc3C@\x8f\x03\xe9\xb3\x11\x00\xd4d\xc5\x83s\x05\x81x\xd2\x17\x01\x17\x00\xf4\x80\x16A\xc3\xeet\x83\x98\x10\xc2\x082\xa4\xb9k\xe7PRr\xea\xeb\xfe\x89\xbd3wE\x13\x85\x12\xe7\xfe\x8f\x83\xe8He\'\xcd\x8f_\xa5\xa90\xf8I\x95\x9aG\xc4b\xa0\xb1\x88\xff\xf3D\xc4\x0e\x15y\x12d\x01\xdcX\x00@\xc0P!\x83\xd3&GO\x99 6\x10%S\xa3\x0b\x02\x8c\x8e\x14-\xb2u\'q\x87@\x0f43 .\x81\x82@\x05\xdai\xd1a\xfc\x07\xa7\x15\x14\xcf(N<;\x0f\\Cv\xf3\xc3\xbf\xea~k\xfd\xdc\xaajK\xff\xf5\xe4\xba]\xd3\x1a\x03\x90\x14"\x01\xcc\x1e$\x8dp\xff\xf3D\xc4\x0b\x13\x18\xa2\\\x00\xee\xf0L\x98J\rDf\x02\x85\xa6+\xa8\'\x1a\x81\x07%J\xd94r!\xa0\xa7e\xa2\x83C"TM\xd1\x14\r\xa4^\xd4\xb8\xc6\xedoQ\xfb\xd9\xdb\xca\xc69\xd7\xc8 P\n\xe4\xca:\xd6\xb5\xe2G\xdd\xff\xffj\x13\xff\xfdJ0\x0c\x15Ec\x07\x01\xe3\x17\x10\xa3\xac\xc5\xa3%\xc43\xff\xf3D\xc4\x11\x15\xc8\x92\\\x01]\x18\x00\tA\xd3\nFQ\xe4\x82\x1f_h~\x05\x03\x12\x8e\x92y"V\xac\xfb\xfa\xacN\xf4\xba\xf5h\xb5\xb5AC\x90p\x11\x88\xf8\x00\xe0\x9d\xe9>8\x10((\x91v\xa6\xa6!N\x85\xb1KUkhC\x15\x9b\xbf\xfe\xf2\x8c\xef\xff\xdf\x10Uo\x0c% ?b\x80\xd4\xbb\x9a\x8a\x86\xff\xf3D\xc4\x0c\x131J\xc0\x01\x8fH\x00\xc2I\xae\xe1\x98\xd4\x87\xf8\x00\x15$\'\nB\xfd\x9e$\xd1K\x9au\xcf\xb7\x0c,\x90xN\xaa\x13\x91Zy\xff\xfdYd/\xea\xa9d\xaf\xff\x9f\xfd^\x010\xa9\xaa\xe9\xe2\x82#\xa6X\xcd\x1f\x9f\xff\xff\xfe\xcf\xd45\xa4\xa9\xec\xe4\x82\xb7\xf2e\xe0^ S\x88\xb1\x88\xceK\x9b\xff\xf3D\xc4\x12\x15\xaa\xda\xa8\x01\xd9(\x01Y=\x8a\x18ia\xfe[\x9d\x0b\x89\x8eJ"\x1c\x01\x85\x84C\xa3\x90:*\x86\x94\xa6\x12a\x868\x8b6k\xda\x86y\x9dK\xba\x9bk\xe5\xfe\xdf\xfao\xb6{m\xff\xff\xff\xff\xff\xff\xfek\xab\x0c\x18\xd7\x0e\x0c\xeaqM\xee\xbf\xea\x9a\xc7\x18\xd8\x88\xf4H\x1e\x10\xef\xa5\xa1\x9c\xc4\xff\xf3D\xc4\x0e\x13\xf2\xde\xa0\x00\xdbD\xb9\x87\x00\xd8\xa7ia\x80V\xecb0\x80K\x118L$\x07|\xcc\xe11\xefR7u\x1b^\x93\xff\xff\xff\xd6\xc9\xcd\xff\xff\xfb\xb6\x8cfB1\x99\x97\xff\xff\xff\xff\xff\xff\xea\xf3\xba\x98\xc1\x08p\xa4\x08\xa1\xeb\xb5}\xb0\x9a\xdd\xcc^#!e\xbdH\xfb\x8c\x00w8\xacx\xed\x19\xff\xf3D\xc4\x11\x11\xba\xd6\xac\x00\xcbD\xb9\xecsS\x00:\xc5\xa9\xe6\x1d\xe2\xe1 n\x91q\x16vN\xf4\x17\xff\xff\xff\xff\xb2_\xff\xff\xff\x99\x0e\x87+\xb5\x97\xff\xff\xff\xff\xff\xff\xfd\xd0\x84\xa8\x87\x10\xe2H\xc4\x08ln\xf5\xfd\xd4\x8f\x81\xa9\xd8\xc2\xaa\xc1\x04\x95\xa4\xed\xb4\xf1\xd6\xee&@\xe6:b=\x80\xc1 \x9eH{\xff\xf3D\xc4\x1d\x12*\xe2\xa8\x00\xd3J\xb9\x94QQ\x81\x82K\xad\xdd\x90o\x7f\xff\xff\xfd\xff\xff\xff\xff\x99\xe7R\xff\xff\xff\xff\xf7\xff\xff\xf7G\xd0\xcaG\x12\x06\x1a1\x84C\x05\x8d\xab?\xd2\xee4\xcc\xc4\xdb\x1crz\xf0\x19NGc\xb8\xd6`\xb0\xe1\xdc\xa5\xcchz\xe5\xc8`=\x92\xc8"T\x82\xd8\xdc\xb3c\xca\xa9\xf9\xff\xf3D\xc4\'\x10\x10\xb2\xa0\x00\xd6\x1aL\xd1u\x7f\x97\xaf1\xff\xfe\x05g\xf4\xff\xf1\xff\xb7\xc1sI\x08\x84\t\x18*\xe0\x82\xaa\xdd\xc9\x92\xc0!\x87\xafC\xee\x8e\x86w\xd0\xf6\xeb5\x99\x9a\x0f[\xa2\x14\x08+\xa82`W&\x0b\xd1\xe5\xa7E\xeaZ\x04\x83e\x04k3?\xb9\xfb\xfbu\xea\xfa\xa7^\xbf\xff\xff\xff(\xca\xff\xf3D\xc49\x121\xbe\x9c\x00\xd4\x04\x94+\xf9/\xfc\x83\x9e{\xfa\x82\x83\xd4z\xe4\xf1hJ\xa5\xb4\xec\x08\xc6\x9e\x10\x82\xc3\xe5\x85\xec1{\xc1\xcb\x9d\x97\x88\x80nM\xfb\x8d\xc1kG>\xba!-j*\x9b\xfa\x98\xc6\xea\xc8\xe9\n<\xa4Qp\x15\xc8\xa3\x1d\x8f\x1e\xed\x1d\xd7\x91\xf56\x8d\xc3\xed\xceHQ\xf4\xff\xff\xf5\xff\xf3D\xc4C\x11i.\x9c\x00\xd6\np\xef\xff]n\x90\xcb\x84 \x1f7\x84\x868\xe1\x03@\x8c2\xd0\xc0\xc0X\x93\xb4)\xe2%w\xab\xa8\xf5\x85r\xa4\x9c\xac\xd9"\xe5\x88K\x92i\x99\x9c\x0e+aQ\x1az\x0b\x0f\x83\xc5\x1a$\xaa\xe2n\xf9;\xf5\xf9\x8b\xe5\xc60\xa5_\xf8\x97\xff\xff\xf8\xc5\x95\xc6\x16\x98\x88\xe0\xe2\xff\xf3D\xc4P\x12!*\x90\x00\xdb\xd0p\x94\xd5\xe3o\t7:r\x10f\xbb\'@\x88\x9do"\x0e\xbf*M\x7f6\xf1\x86\xe0x2`\xe0*D\xc6\x05\n*\x8e\x0c\xbd\x05\xbb\x8aV\xb7\xd5\xbd\xd9\x8e:\xa5F\xaci\xf7\xd3\xfe\x14W\xff\xfe\x94\x9bR\xad\xa1\x83\\&J\x01\x12\x1c\x04Z4\x1acj\xdej\xe3\x81\x00\xff\xf3D\xc4Z\x11\xf1.\x8c\x00\xdb\xcep\x05\xb7\xccw\n/Z\x96\xb5\xf8R\xff\xd9\xadL+\xda\xa3\xb2\x88B\xede\x03\xb58Lw\x94\x8dRw\xed\xfa\xff\xfbX\x9a\xaa\x03\xc58\x8f\xff\xff\xff\xf4*&l/R\x9a\x9fP\x03\x17\xa7=Va v2\x1468\xb4s\t\x17\\l\x91\x0e\xf5\x8aE\xc8\xdbo\tD\xff\xf3D\xc4e\x11i*\x88\x00\xe3\xd0p[\xe5\xb7k\xf0\x08\xaaw\xac\xba\xcc\x02\x02V]\xe0\xd2\x83K\xd1\x01?\x0c\x97+\xff\xff\xfdrg\xc1\x00\xc0!.\xfe\xca\x04E\x9e\x9dUs\x86A&\x13\x08\x98J\xb2bph\xd1\x10\xb2\x80\x84!\x92\xc0@\xa0,>\xc3P\x1f\x13\xb4\xd0\xdd\x8a\n\xb1+\x1fZ\xbe7\xb4\r\xff\xf3D\xc4r\x12\x18\xaa\x80\x00\xde\x18L<\xc5l\xb0\x13\tQ\xe2\x87V\x1a\xfe\x1a\xff\xfa\xaaln\xa0\xea\x80\xc2PT\x15%\xfd\xff\xd2\x02\x19\x9a#\x80P0\xd4\x95R(\x16,\x1c\x1cb\xa0B\x82j\xf1A\xc1\xc0\xa8G\xa5]\x1610\x96>z\xb3\xb6\x0b\x0b\x0b#\x06\xc6\xfa\x90[(\x05P\x99 \xe2\x94K\xe9\xff\xf3D\xc4|\x11x\xa6t\x01\\\x18\x00\xd4\xc4y\\A3as\xfe\x87\xb0^\xc0\xe4\xc4\xfeF\t\xd0\x9b\xfe\xdf\x8b\x01\x0f"b\x80"\xa3\x8cs?\xff\xec3\x07E(\xc5\xc2\x91:,\xb2\x13\xff\xff\xfc\xd8\x9c \x06\xa9\x90s\x87\x96\x91\xa1\x87\xff\xff\xff\xf9\x89\x07,\x9fb\xd0\xb3\xc7\x19\xd3ssS\xe5\xca}b\x8f\xff\xf3D\xc4\x89!c*\x80\x01\x9b\x90\x00\n\xfd:\x12e\xd3n\x13\xc2i\x08\xcb\xddF\x0c\xa0\xcd2\x1c\x902\xd7z\x9e\xab\xfe\xd9\xedn\t\x8d\xa6\xc8\x884j5\xabxtU\x0e\xb1+\xe1f\xa5\x08)WH\x85Me-/UWR\xff&\xd5Nri\xe1\x01E\x07^\xc8\x88(\x97\xa4\xf1C1b\'\xa2\x9dG\xff\xf3D\xc4V\x19iF\x9c\x01\xd9H\x00\xbe\xbd\xf4\xbc\x1a/c\xae\x02-D\t\x07\xe0\xff]\xbbn\xa9 \x82"\xe3\x1d\x8c\x12d\xe2\xcci\xc3\x07:\xfcH\xc2\xc3\x0fR:! \x10!\x9aH\x1c:\xac\xd0\xf3\xd9\xcf\xcb\xe5\x8fP\xf3V$\x02-\xd2\xa4\xf3\xb4\xf5f\xbe\x9b\xf17\xa0\xb0@\x08\x1f*\x11\x98\xc8T=\xff\xf3D\xc4C\x19\x82\xf2\xa0\x00\xca\xca\xb9\xa6\xdb\xff\xd9Z\xca$\xc8t\x13z+\xff\xff\xff\xffVl\xc8\xf4\xf4\xef\xb3\xbd\x91\x0c\xaaQ\xcfaW\x0c2\xe9\x9a\x98\xedV\x04G\\\x8a\xaa\xa8\x18I\xbc\xf6\xf68<&]8#`\xd0jJ\x14\r,)\xaa\xc7\x16\xfe\xeb\xd3\xc2\xfb\xf8o\xff:kW\xbbbv\x8e\xc5I\xff\xf3D\xc40\x1ba\xc6\xa0\x00\xce\x16\x94\xdbd\x82\xc15\xe4\x82\x19\xcd(2;r\xf9\xbaMj\x91\x12\xd8\xbbQ\xa8\xa5/\xab\xfb\xaf\xf6\xfd\xd5\xd3\xeb\xcd\x14\xa3\xefB.S\x05\n\x08\xbf\xd1\xfd\tE(\xa6}\xc5\xd0\xe9B\xc5\xd0a\xc1\xd1\xe1\xb5\xa6\xc7\x01\x90\x8b\xba\xfd\x98\xd0\xfa\xaa\xdax\xd3\xaa\xfe>T;\x99I\xff\xf3D\xc4\x15\x16\x01\xb6\xa8\x00\xc6\x0e\x94#\x18\\#U\x142Eja\xc8\xcf\xfb\xddo\xeb\xd1g\xaa\xb0\xbc*R[\x9d\xe9\xc0\xb8\x93\xc6\xe4\x8f\x11\xc1\xf1\xb1\xc1\xa9\xaa\x85MbzN[\xfc\xee\xad\xffz\xd58\xf8\xe1\xa6\xc1)/\xff\xff\xf4\xd7\x15\xbf\xb6\xd5\x91\x83\xf6\t0\xf5\xf6\xc2\x13\xcdw\x1d\xf1}\x91\x02\xfa\xff\xf3D\xc4\x10\x0f\xc9\n\xb4\x00{\xd6pw\xc5\xb0\x08\xd1\xde\x9de\xe6\x93\x98\x0b;\xbb\x1f\xdf\x1c\xb8l\'&V\x1b\x9c]S\xf5\xecu\xc2\xbfd\x83d\xe8\x98y\xe4\xdc\xcf\xffm\xca\x11\x1f\x0e\x8b*\xc7?GT\xd9\xbd@"\x13B\xc7M\xad\x1f\xed\x81Sc\x01\x96jE\x8bH\x12L\xeemmj\xde\xce\x03\xa6\xd5\xff\xf3D\xc4#\x11\xc9\x06\xb0\x00\xc6\x12p \x86x\tt\xe0\x10=5\x04\xb3\xd5\xe5^\tW\x80\x85\x99\x11\x80&d&\xb3\xff\xb2\xd8\x95a\xd6\xff\xff\xff\xff\xf5\xd5\x9b\xd88\x03\xd4[\x02\xba%\x19\x84\xb4\xf9\x8a<fx\x142\x1b\x9e\x1fFM\xd8\x08b\x86=N\x0b\xf4\'\xe9\x85\xc1\x17l4Y\xee>\xef\xe2\xcc\xf7\xff\xf3D\xc4.\x11A\n\xac\x00{\xd8p\x96\xa7\x18\x1f\xb1\xb2\xf8\xfd\xb8\xc5\xa4\xa7\x7f\xf26\xc5\xa6\xa8\xff\xff\xff\xfd\xeb\xed\xf8 \x97T\x94\xd2\xd2\xd6\xdf\x97\xc4_\x89m\xd5/\xd0\xc0X\xaa\x1a\x12\xe3\x95@\x890\x8b\x13\xf8\xcdhLz\n\x97\x914A\x80|\x16\x99\x8ep\xcd\xd4\xb3\xe2\xdbp"\xde\xe1S\xfa\xc9\xf5=\xff\xf3D\xc4<\x10\xb1\n\xa4\x00\xc3\xd2p\x7f\xfa\x8fG\x96<Y\x85C\xefY\xcbI@\xb5\xd6\xd0AR8-b\xc5r\xce\x95\x8dpd\xc0\xb4h(\x80Q\xa0"\xd2I=\x0f.Y\xe4\x81\x81H\xf2\xab&u\x99\x18\xaeUc\xa5\xc0\x90\x13\x00=}\x7f\xff\xf3\x14\xe3\x9e\t\x7f\xff\xff\xff\xfe\xec\xb7*\x80\xdf\x82QH\xff\xf3D\xc4L\x11\xb9\x8e\x8c\x00\xc9\x84\x94\xc9x\xe1\x9aH\xd5\x0c\xaa\x1e\x94\xce\xcb\xa9\x91\xa0\x99\n\x01T\xd8#\x81t\x89\x8c\xab\x01\x15\xb6\\\x05\x15L\xa9*\xe6-\x8fpDv\xd1\xd7\x14\xe5\n$\x85\x01\n\xc0@@L\xcaOz\xff\xf5dA`(\xa3\x06?\xff\xf4U1%&\x16Iu\x12\xba;\x10\x87\xad\\\xde\xff\xf3D\xc4X\x12I\x9e|\x00\xcaD\x94\x1a\xb5\xa6\xa4\xb4d\xfaE\x144\xcd\xa0\x13\x02)\x13\x15\x14\x06\x8f"\x94\xe2\xb3q\xbd\x95=2\xf2\x9532\x19@b@Jk\xd1\xdbG\xff.`#;\x05 \x10t\xea\xd5\xa51\xa58\tY\x05\x92Mh\x06w\x1d\xca\xadh\x92\\\xd0\n.D\x02\x12G\x0b\t*M\t\xff\xf3D\xc4a\x10\xf1\x9a\\\x00\xc2D\x94)&(\x15\x00\x18\xc1f\xd6\x94T9\x16\xbfUZ\x8a\xf6\xe1\xbf\xf6\xb1SH\x88\x80\xa0\xa9\xd9\xd9`jYAW\x15\xd6\xff`*uo\xff"0\xb0\x81%\xecG\xf5`_\xedY\xb6r_X\x02\x1f\x1c4\xce\xd2\xaa\xac\x9d\\\x95,t\xea\x06\xe1\xb8\xca\x1804r2\xfe\xff\xf3D\xc4p\x129\x1a,\x00\xc9\x90p\xcf\xd9C\x02\xa0\x99\x93#EL\xb8Y\x9c\xc0\xae*\xdf\xa0\x19\x15\x12\x1a\xc5\x1b\xf82($\xff\xeb\x16mB\xf5LAME3.100UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUULAME3.\xff\xf3D\xc4z\x12\x18\xe1\x98\x00\xc2Fp100UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUULAME3.\xff\xf3D\xc4\x84\x00\x00\x03H\x00\x00\x00\x00100UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUULAME3.\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00100UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUULAME3.\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00100UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\xff\xf3D\xc4\xac\x00\x00\x03H\x00\x00\x00\x00UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"""
'''
with sr.Microphone as source:
    aud = r.listen(string)
'''
aud = r.listen(string)