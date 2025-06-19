from pathlib import Path
import gripql
import os
import orjson
import datetime
import copy


DIR = "META"
SCHEMA_PATH = "calypr-schema.json"

RANDOM_PROJS = [
    "/programs/cbds/projects/01f04710420544a998ee7bcd90fa5e7d","/programs/cbds/projects/029c9f64abd94b9584823154daa95cd8","/programs/cbds/projects/02b379ab10e84c439e8c615bbd98d1c0","/programs/cbds/projects/03bc2b4ade1840b18b5c93b33b39b7bd","/programs/cbds/projects/049224da3f71483b861bd7ef54862998","/programs/cbds/projects/095b1366e22440b380fdc16ca5584708","/programs/cbds/projects/0a7b72d205ab49a58bf17c20543d05e9","/programs/cbds/projects/0b07124d9f5b4d9baeea12088d6d1671","/programs/cbds/projects/0b655c995e5243ab8febadb4a02131f3","/programs/cbds/projects/0be5517717e1483db9546e1783b24917","/programs/cbds/projects/0d3c5f0b18bc4ac98e027879141c8b60","/programs/cbds/projects/0d41ceea0bad41a68144b4cc678895cc","/programs/cbds/projects/0d8d7c6364d3425ca7cac91ff44ecb0a","/programs/cbds/projects/0e959b9959974fac8021cd46a8e5f7d7","/programs/cbds/projects/0fce179c9a854f00ae76cf462e597e50","/programs/cbds/projects/102bd19e1c254337b1d826688364b18f","/programs/cbds/projects/117b9d618c9e4b8ea06bfa57e024ed7d","/programs/cbds/projects/125905a9f67946148dce0cf5e1dcc9c0","/programs/cbds/projects/12b86874f7bf49308e2c5ac4476403df","/programs/cbds/projects/13d4ab94de8f4d18a77d0994df1ed12c","/programs/cbds/projects/148886aec6d242e8a38a6c43bb7e9dca","/programs/cbds/projects/151e630e6073491885c603df17822290","/programs/cbds/projects/15854867ebdb439ab9578f6077eb2961","/programs/cbds/projects/15dd50da0e0f4c00b59b37690fb80d9d","/programs/cbds/projects/1638a55997f14ea1acc4bae51df4b0f1","/programs/cbds/projects/1640fc254448480c8e9544348e22d938","/programs/cbds/projects/179d760c6aa8418eb8dc93a62f348175","/programs/cbds/projects/19089b5b70e3477c850b5ee2351065b5","/programs/cbds/projects/191d022c33d94a0a94dd66cbc609733d","/programs/cbds/projects/192f1e6d99c541bb9aa9d511a4686d94","/programs/cbds/projects/196dfc6c1a6e484081f1327a19dff6d0","/programs/cbds/projects/19b67c49c73d4a39bf10ff68ea38c761","/programs/cbds/projects/1a8055b7e8434d8197e1e171099116b3","/programs/cbds/projects/1adfd6cab4f94b658714d4047833e1ad","/programs/cbds/projects/1b337c768be5457f9a281ced521f52d6","/programs/cbds/projects/1bc1405a52ee468cb512613c4d2ef83b","/programs/cbds/projects/1d561b3471fc4bf78863d75ea0e7ac06","/programs/cbds/projects/1dec0d551a174cbca63501aabd690ed9","/programs/cbds/projects/1e398394d20049edadeef42001d3eac7","/programs/cbds/projects/1e5b4c9d09814c8d84a0e5ee2e5ccb30","/programs/cbds/projects/1eaef1025e2c472bb8088de120bd0b95","/programs/cbds/projects/1f0aafee47cb4790af08def23fd0320a","/programs/cbds/projects/2023088914b34912a332a3780d420e52","/programs/cbds/projects/20dc47cd023b41d39e88879b0b915646","/programs/cbds/projects/26a0908eea2d47aebf2c8144f3cd4f71","/programs/cbds/projects/273ac3451dc34399a5584c1831f3c61c","/programs/cbds/projects/282f76255c994c0dbc14585ee62a16d3","/programs/cbds/projects/295fa9cdffbd422e921d4c4cf91ff4c1","/programs/cbds/projects/29687dc527cc47dc9b53b9cc5cc06517","/programs/cbds/projects/2a64cca9725e40fa8a6e26ca23160800","/programs/cbds/projects/2ad55b5c90cc4181afe782adff896b6b","/programs/cbds/projects/2b9eb14483564a2891c58a779b42d4e9","/programs/cbds/projects/2ca8381e5f5d4d72baec9d49e908f1ca","/programs/cbds/projects/2cba15fb061a4bc5958ca2ac537a86c1","/programs/cbds/projects/2d90c4683f8144dc9f0d89ee7436b245","/programs/cbds/projects/2dd620480c914dbea3a97e01890fb780","/programs/cbds/projects/2e3e0d78155f42eab3cf78e295dfe251","/programs/cbds/projects/31ac464eec9846569d1ca2cb177a884d","/programs/cbds/projects/323e0bcf8c4e461ab04dd7fea3d6507e","/programs/cbds/projects/344d02b6d32b44e680ffcc82f8281f32","/programs/cbds/projects/35047ab90a644d33abd7abc2e20cdcc2","/programs/cbds/projects/3685c16e451f4d10bcede225864527c0","/programs/cbds/projects/36ad77a24e42414a88a1219399f1673b","/programs/cbds/projects/395bba2c60314bdcbd4bafb9b5917ae3","/programs/cbds/projects/39c1c40c17984c8dbc408da2f87cee23","/programs/cbds/projects/3a4a530616a34d5d9e60074e0f2b7c4b","/programs/cbds/projects/3a759ab866a345cc8a23df17f9655b8a","/programs/cbds/projects/3b2b2dc86e5847ea8ae926e8dbb6ab55","/programs/cbds/projects/3bf6392153ff4c61bb607bedfe52a0ff","/programs/cbds/projects/3dcacae31a64451c8c790951bc49bdc2","/programs/cbds/projects/3e4f901c5ba8460b82f5d5aa62070215","/programs/cbds/projects/41914c248fae49ea8d9e9d6fbf019088","/programs/cbds/projects/42a98e5af078471984fab4b6ceac1341","/programs/cbds/projects/45cf4bcc7cb7491eb52f6b3f6b646f99","/programs/cbds/projects/4681217813254e699a519158ed4065d2","/programs/cbds/projects/471f9e25f2484b729d9492312f9690af","/programs/cbds/projects/485e77017c9e48d387c3df0e9f199be1","/programs/cbds/projects/4a005858f7b447eda0c5742e809880a8","/programs/cbds/projects/4a09f531cb23495497ee15ff563ed561","/programs/cbds/projects/4b0082556c7c45958357da876c0dac5d","/programs/cbds/projects/4bc394ecf86e4bfc92e2fe7859d752b8","/programs/cbds/projects/4c56540f30a1425bbbc2a3142aa629f4","/programs/cbds/projects/4ceaf2b28e564930b7d61c0f1a1fc6bc","/programs/cbds/projects/4ec6806eb1e6459cbdd7280441ac5ead","/programs/cbds/projects/4f795b952c7b47a4b09c1ee15a5aa40d","/programs/cbds/projects/50223cea66df48b98c1ac89ad6d44ebf","/programs/cbds/projects/5136f39e019e4849ab32ddb4604dab49","/programs/cbds/projects/52cc09e2d9ed4eaabd8c0181a739da6b","/programs/cbds/projects/53186a2e3dc44f398379f37121ac2415","/programs/cbds/projects/536cbe2af63a4d7fb814f0273dbaec21","/programs/cbds/projects/53d172305f1040b09bc92af0a6f96bbd","/programs/cbds/projects/548ac72921364fd6ac0cfe35fc5f56e7","/programs/cbds/projects/557465442796446b88f292b18262ebe2","/programs/cbds/projects/5792450901694b498aa6ee91f00fd481","/programs/cbds/projects/579d8ef33b664b4ea081e47d99da7e35","/programs/cbds/projects/57b342259c654f1c934b00bd4e7eaf3c","/programs/cbds/projects/58010a11954b45f1bba249daac3f0f55","/programs/cbds/projects/5e189542831f4c6ba3ccb1d6bee3fcc5","/programs/cbds/projects/5e3ddaa4094c4ca0b10fac60eb1eaf9f","/programs/cbds/projects/5f5f6be98a264f9e8b3b3c27b7e0c5ad","/programs/cbds/projects/5fa24aad2f6c450b8ba0441ad7b569ed","/programs/cbds/projects/61b018873d314941b1ceb2066467a4bf","/programs/cbds/projects/62be5275f11c40348de15ba0873d78a0","/programs/cbds/projects/63f3abe54b50414daf12b2b2d0e562a6","/programs/cbds/projects/648e47f6d6e44d19b843496cce119014","/programs/cbds/projects/6576a256220b4a09a84ee2434c3f5857","/programs/cbds/projects/65f8c249051447eeace55272034f7caa","/programs/cbds/projects/668e0eb572514535b70a73f67a7142ba","/programs/cbds/projects/6693a2596ae240ee8993a32f74b7ec43","/programs/cbds/projects/67adb3d9a3b84110807e88e10266e5c5","/programs/cbds/projects/68c9072f3d2f4296987f1262f89cc1b1","/programs/cbds/projects/68ebc1259a7b493196c86e5eac6d7039","/programs/cbds/projects/6b91cf1688cc401791cc7a635f7fe59c","/programs/cbds/projects/6ba48d4e19dd49f28c578c716ef12c09","/programs/cbds/projects/6d04d597bc354dd8a7ea670368979937","/programs/cbds/projects/6d1d7d06b7784142b859beca17b4aef2","/programs/cbds/projects/6dab4eb91a554cd69fdb25d8504f994d","/programs/cbds/projects/6eedaf1b55d44784a8618838ecdff760","/programs/cbds/projects/6f6ca0629c2d40b7bff238b500bd97d7","/programs/cbds/projects/6f7000ec54ac4df796c4e8b0f5302df0","/programs/cbds/projects/6fe19c1192d047a48dbe1425c4c1bf9b","/programs/cbds/projects/7044ab7b2ea8435581bb1f363ec4efc7","/programs/cbds/projects/7093fa00d90b48618552019fb4cc4325","/programs/cbds/projects/717af3222b254ae1b9a2e92d51b49656","/programs/cbds/projects/717e2378196046cebca0f3d4556c0390","/programs/cbds/projects/71973618ab9541b1ac68fa1e421e17b0","/programs/cbds/projects/71ba11f78f694489b5c349a9d3856a93","/programs/cbds/projects/7262f69d5d4743b68dfcad15c3e3cec0","/programs/cbds/projects/729bb213dcf0485c9f939c55b7397d38","/programs/cbds/projects/73ed40d6c1614715952a8baf3c84268d","/programs/cbds/projects/749d7092d29b49819e8d626d6a458b7d","/programs/cbds/projects/74e28c68bc724956b5b2690c77270063","/programs/cbds/projects/774afbdd3cbf480da405d3d60f797b36","/programs/cbds/projects/77b3229985d6497c808adcca9e48e8fc","/programs/cbds/projects/78444db2428b45e4969152d0479b7886","/programs/cbds/projects/7cce4174638f45a5a05305feead714a4","/programs/cbds/projects/7d1f1ad2b3314da1acb99e70145d5891","/programs/cbds/projects/7e198489cf7c478180d02927fb55bf62","/programs/cbds/projects/7e4d2bbcf67840a7b91f2fc974b49070","/programs/cbds/projects/80efd0ab78c34c61bc09b0d46d93dd74","/programs/cbds/projects/8194744aaf1546f086386374215f6dc6","/programs/cbds/projects/82e897c21ea945fbb8d8ab52a3f0fd24","/programs/cbds/projects/8388215ed8ab49b2b1b2e94fcac38f44","/programs/cbds/projects/83ec93171d8c4bcb93155f39677b2e5d","/programs/cbds/projects/857c64e6315f4d248682dbf18db2604b","/programs/cbds/projects/858fce0f5877483c840b2436cd657f60","/programs/cbds/projects/86b471103cea4017a932d569bc034d77","/programs/cbds/projects/873cb70cce5045e9806442004047f663","/programs/cbds/projects/8836a3b1b0844e2b8fee0b90f92ebc7b","/programs/cbds/projects/8892fb2774ab4bd185b7917b68a4b33a","/programs/cbds/projects/88d60e9744a64672b81c5653070447bf","/programs/cbds/projects/89d5db39bb864da49aad49560a713839","/programs/cbds/projects/8a80b513a9314906a28b81117d6e336b","/programs/cbds/projects/8af944806c9c4791b46f960841c5a17f","/programs/cbds/projects/8c945f774f7d47299c636473f7583262","/programs/cbds/projects/8d8dae991df74d4ea11a66b513872d42","/programs/cbds/projects/8e145d879f4a41f39bc7e4e731f3a84f","/programs/cbds/projects/8eab2fb65158434b888b13d7df7a02e4","/programs/cbds/projects/8ecb3d4af28b4291a38e6e16b99041e9","/programs/cbds/projects/9008d0e15b5a4df4ad1abfdeed77b8df","/programs/cbds/projects/907df4f967ac4954b1752056ea9896d6","/programs/cbds/projects/92d864f92ac2449f8ff6f27807a6e8fd","/programs/cbds/projects/932b421a890c4b9fb04278c75899799d","/programs/cbds/projects/93a2b0a03ddf4b348dc86400b2431886","/programs/cbds/projects/93cbd00ed57b42298a4028a4bc05d58b","/programs/cbds/projects/947971225b1347878f27f745e33e1fe5","/programs/cbds/projects/96cf6a90caaa4b289a5fd50924b8b042","/programs/cbds/projects/98b64635cf8445809a648de760414565","/programs/cbds/projects/98e10b32a1c9448881e40f0bc21eb7a9","/programs/cbds/projects/9942128400084d0592208fa3099a41ad","/programs/cbds/projects/9c48d47e120e423ea4109e667c74ff63","/programs/cbds/projects/9e5bf5374889450e9f4a6fa39677fd0c","/programs/cbds/projects/9ef2c139c65d4d25b45a91a27b81c3d7","/programs/cbds/projects/9fe539c4fc0849eba87508161534c676","/programs/cbds/projects/a1a5e7a29ca64af5bfc1b1245717f9f3","/programs/cbds/projects/a1c2cb3433aa40b59ecdc3d412702376","/programs/cbds/projects/a1f2b70afab14a8d80c6f068f27af4e8","/programs/cbds/projects/a24a51d0eb2c42d591df09c2e793ed6d","/programs/cbds/projects/a25bae0df8e84a6d979c6bbc0df328e8","/programs/cbds/projects/a2a68d35e19a428fbc7feefd2830333d","/programs/cbds/projects/a2f3f14bc74f44dfba8766948090d126","/programs/cbds/projects/a3058ac416ed4ee5a58778b84c79e17a","/programs/cbds/projects/a3e31e20856e4f808cb45b701f8186de","/programs/cbds/projects/a4a45ddb980443a49d63d84f9d35b6b3","/programs/cbds/projects/a505f4d4192e4fbe97c83b48f73c724a","/programs/cbds/projects/a86a00c256ef4d5f94eb997c1168135a","/programs/cbds/projects/a978082cac484984bc4346606841be77","/programs/cbds/projects/aa5dcde7c9fa43079ff3525b455a986b","/programs/cbds/projects/aa6dc6c396904c138fe45536551a8056","/programs/cbds/projects/aa794f4e1daa42bcb2a74ae863a49c29","/programs/cbds/projects/abc35dca80c04bd6853989856301f3f3","/programs/cbds/projects/ac016ff8d04f4dae8416d1c1b214c5c1","/programs/cbds/projects/ad760775181e4b2a906ce0b342ce5e6a","/programs/cbds/projects/adf734289f9741f3921a5bc5eef332df","/programs/cbds/projects/ae5122f0c9c644b981d0ebd981c01fa9","/programs/cbds/projects/aecd8f13912d4ad5a581819f72c15570","/programs/cbds/projects/aeda8279c3a74f839b83d28ca8109acc","/programs/cbds/projects/aef81c0aab4b4e99a44a32d9cd256540","/programs/cbds/projects/afdd5bd0269442968783a7a7957f8953","/programs/cbds/projects/afed389d36904de8a36b3336bc3fff3b","/programs/cbds/projects/b0ac9891170c4b438bbbab8e9d7150f5","/programs/cbds/projects/b0d8b364ce604b75b2b55a4187f3d3e8","/programs/cbds/projects/b0fe4b80517d4e05b2294ca5fb639d08","/programs/cbds/projects/b1666618e8674c4f9e813dffadd23df0","/programs/cbds/projects/b1939c9874014f6c96c84c56da70db46","/programs/cbds/projects/b520bc0c3e1e40b6870de48318ab053b","/programs/cbds/projects/b55a275ea17145518a3749ffdd1e38d1","/programs/cbds/projects/b7ecb5e667194fb5a06184afc10ad3ac","/programs/cbds/projects/bb0463565fed423dbfe6d47a058d4717","/programs/cbds/projects/be09bfc496fb472181602d78a9f8a08f","/programs/cbds/projects/be217d9c784b44048d87af2f21c636c7","/programs/cbds/projects/bf1ce319ea2548949531d705935ae1c5","/programs/cbds/projects/c0ce789b42374406bae1b8004bd26f06","/programs/cbds/projects/c12f8fdcafed4003bf4fbe89fd683e82","/programs/cbds/projects/c18c3be4fb4a420fba47cbd4f99c94bf","/programs/cbds/projects/b7ecb5e667194fb5a06184afc10ad3ag"
    "/programs/cbds/projects/c3661db48ae346b791078f2a785b41b7","/programs/cbds/projects/c3cfc07649e3410797df69947f9f2fbf","/programs/cbds/projects/c506396b78d84807b1b7b3e256484510","/programs/cbds/projects/c5fb284e1a6d4e30ad2060cd34afcd5c","/programs/cbds/projects/c61208eb676a4040944a341282e481e0","/programs/cbds/projects/c72d6bc8b40d43d191eeb84e7f1d4b4b","/programs/cbds/projects/c88319276def4610864601e37ec754ac","/programs/cbds/projects/c8b8d99a82304251a11e2e38d3a7602e","/programs/cbds/projects/c905fa0386754e6596e20e7c85484741","/programs/cbds/projects/c90d092c25084affb9e341658df25930","/programs/cbds/projects/c985fe57fc0444a188c35265e45f9db4","/programs/cbds/projects/c9b1aaac2e70484fbd1d7a915fb10a4e","/programs/cbds/projects/caee46a6464e42aa977e17bf1c4d5531","/programs/cbds/projects/cb9991e92d0c4bb69e67664ca9477370","/programs/cbds/projects/cc13f09d2ca944f79535d51a1c870623","/programs/cbds/projects/cd0ae72e9e314653a752f9f234ffc11b","/programs/cbds/projects/ce4594ac431149e3982724a73f84176b","/programs/cbds/projects/cee7ab078ce74ffe8b37718c0c1a9fad","/programs/cbds/projects/cfaecedf0acc459593cd44f81325745f","/programs/cbds/projects/d0fbd452ed014c04aadf89aa34b96362","/programs/cbds/projects/d1e8b511da0346d499c64f52fa659e3b","/programs/cbds/projects/d1f140bf246b4f53a984488707c91745","/programs/cbds/projects/d27bfd2801844dccba3a9b109dc4f17d","/programs/cbds/projects/d284599fc61844a6a0c88f7b3239953d","/programs/cbds/projects/d396342183db41eca1c6cf35aa280cd0","/programs/cbds/projects/d3d395315a2a43d79b14034e51c6c00b","/programs/cbds/projects/d62ba1645d3b468b8519e2e0b6276033","/programs/cbds/projects/d6ea0306bfe04c9caf2c5592f7087182","/programs/cbds/projects/d74beace61d94cc7a79aad6aceeedee1","/programs/cbds/projects/d75fcf162a984c3fb01895e36ba4947e","/programs/cbds/projects/d8221ff0536f42c08904bdea3cbc1ea0","/programs/cbds/projects/d8fea54583bd454cb547e6bf86cbbf58","/programs/cbds/projects/d920c56ae83d455b8345469e20674472","/programs/cbds/projects/d9fbb4589ef54a729a723be57f20d1cf","/programs/cbds/projects/da49c65e136c4094aff399483ea8cb8c","/programs/cbds/projects/daf0e049a536461b901b79fb285ae672","/programs/cbds/projects/dbea537f1e704b23975bdb1fc61c0ac3","/programs/cbds/projects/ddbc3605419f4e92ac3398929e405202","/programs/cbds/projects/de91c382c2134b108f56caa2e8b4aec2","/programs/cbds/projects/df2d92798b1545669573ca6200cc8bf1","/programs/cbds/projects/e005b7568c894987b9bb5efe20740587","/programs/cbds/projects/e220dc0b5d39459ab3baea812e090dfd","/programs/cbds/projects/e2d040ee48c441da9e5e24b9ccbd8e4d","/programs/cbds/projects/e2ec71832c1e4b11a81e653e1dc18077","/programs/cbds/projects/e47f03b16edc428aa1ebb50ae4f0ab28","/programs/cbds/projects/e68671760f33426c96455b8971c4f32b","/programs/cbds/projects/e6c657e127bd4995b010092af88b13fe","/programs/cbds/projects/eb811380ddce412b8de867401e3e12ed","/programs/cbds/projects/ebbf73831ad547fbadea3d3ebdfd5ec3","/programs/cbds/projects/ec0eea13f66245648d5ff7d5a4b5f6bd","/programs/cbds/projects/edbabacf543b4ec2b874dcd61fb84c25","/programs/cbds/projects/ee5d869cf63c493a932293948706bd4c","/programs/cbds/projects/ee9effab99694ede8bdf6c398542a170","/programs/cbds/projects/f02fe2c131374ca1a10f88532855f0d3","/programs/cbds/projects/f2381c8e42b04e0f8d4cb44fa58dd0d1","/programs/cbds/projects/f2c25768577144ca8ad2e8b9c595b7c3","/programs/cbds/projects/f45ebb6425364237a63809c60c78a28f","/programs/cbds/projects/f810204e556049c9bc1e7d6381307b2a","/programs/cbds/projects/f8bf9e752568413aab11709a8e7dc29a","/programs/cbds/projects/f9a7db9f59c1444da9537046cd9cb56c","/programs/cbds/projects/fa8e8685a7924b18ba0ce7e2edfb6de5","/programs/cbds/projects/fd150451430d49fe956421278544b0b3","/programs/cbds/projects/fea8250c475c43708899c1c8cfaa5ae3","/programs/cbds/projects/ffa45c7f5c8448d3b1977451a64deb59"
]

def load_json_schema(path):
    with open(path, 'r') as file:
        content = file.read()
        return orjson.loads(content)


conn = gripql.Connection("http://localhost:8201")
#conn.addGraph("TEST")
G = conn.graph("TEST")
G.addJsonSchema(load_json_schema(SCHEMA_PATH))


###################################################################################################
# Load Dataset
###################################################################################################
T_LOAD = datetime.datetime.now()
print("Benchmark Start ", T_LOAD)
for file in [file for file in os.listdir(DIR) if file.endswith(".ndjson")]:
    T_FILE = datetime.datetime.now()
    with open( Path(DIR) / Path(file), 'rb') as f:
        bulkRaw = G.bulkAddRaw()
        count = 0
        extra_args = {}
        for line in f:
            count += 1
            line = orjson.loads(line.strip())
            if count % 5 == 0:
                extra_args["auth_resource_path"] = "/programs/calypr/projects/test"
            elif count % 9 == 0:
                extra_args["auth_resource_path"] = "/programs/calypr/projects/testtwo"
            else:
                extra_args["auth_resource_path"] = "/programs/calypr/projects/testthree"


            bulkRaw.addJson(data=line, extra_args=extra_args)
        res = bulkRaw.execute()
        print("Loaded: %s in %.2f seconds" % ((Path(DIR) / Path(file)), (datetime.datetime.now() - T_FILE).total_seconds()))

print("Loaded Test data in %.2f seconds" % (datetime.datetime.now() - T_LOAD).total_seconds())
print()


###################################################################################################
# Queries
###################################################################################################
# 0.    V() query

print("query 0: #################################################################################")
T_0 = datetime.datetime.now()

count = 0
res = G.query().V().count().execute()
count = res[0]["count"]
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_0).total_seconds()))

###################################################################################################
# 1.    HasLabel Query

print("query 1: #################################################################################")
T_1 = datetime.datetime.now()

count = 0
for i in G.query().V().hasLabel('Observation'):
    count += 1
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_1).total_seconds()))


###################################################################################################
# 2.    Has Query

print("query 2: #################################################################################")
T_2 = datetime.datetime.now()

count = 0
for i in G.query().V().has(gripql.eq("auth_resource_path", "/programs/calypr/projects/test")):
    count += 1
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_2).total_seconds()))


###################################################################################################
# 3     HasLabel.Has Query

print("query 3: #################################################################################")
T_3 = datetime.datetime.now()

count = 0
for i in G.query().V().hasLabel("Observation").has(gripql.eq("component.[0].valueString", "Post-treatment")):
    count += 1
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_3).total_seconds()))


###################################################################################################
# 4.    Calypr filter query

print("query 4: #################################################################################")
T_4 = datetime.datetime.now()

count = 0

projs = copy.deepcopy(RANDOM_PROJS)
projs.append("/programs/calypr/projects/test")

for i in G.query().V().hasLabel("Observation").has(gripql.within("auth_resource_path", projs)).as_("f0").limit(10000).render({"auth_resource_path":"$f0.auth_resource_path","component":"$f0.component","id":"$f0.id"}):
    count += 1

print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_4).total_seconds()))


###################################################################################################
# 5.    Calypr traversal query

print("query 5: #################################################################################")

T_5 = datetime.datetime.now()

for i in G.query().V().\
    hasLabel("Observation").has(gripql.within("auth_resource_path", projs)).\
    as_("f0").outNull("focus_DocumentReference").\
    has(gripql.within("auth_resource_path", projs)).\
    as_("f1").limit(10000).render({
        "auth_resource_path":"$f0.auth_resource_path",
        "component":"$f0.component",
        "focus":{
            "__typename":"DocumentReferenceType",
            "auth_resource_path":"$f1.auth_resource_path",
            "content":"$f1.content",
            "id":"$f1.id"
        },
        "id":"$f0.id"
    }):
    count += 1

print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_5).total_seconds()))


###################################################################################################
# 6.    Calypr filter + 1 traversal query

print("query 6: #################################################################################")

T_6 = datetime.datetime.now()

projs_two = copy.deepcopy(RANDOM_PROJS)
projs_two.append("/programs/calypr/projects/testtwo")

count = 0
for i in G.query().V().\
    hasLabel("Observation").has(gripql.within("auth_resource_path", projs_two)).\
    as_("f0").unwind("component").as_("f0").outNull("focus_DocumentReference").\
    has(gripql.within("auth_resource_path", projs_two)).\
    as_("f1").select("f0").group({"component":"$f0.component"}).\
    as_("f0").limit(10000).render({
        "auth_resource_path":"$f0.auth_resource_path",
        "component":"$f0.component",
        "focus":{
            "__typename":"DocumentReferenceType",
            "auth_resource_path":"$f1.auth_resource_path",
            "content":"$f1.content",
            "id":"$f1.id"
        },
        "id":"$f0.id"
    }):
    count += 1
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_6).total_seconds()))


###################################################################################################
# 7.    Calypr 2 traversal query

print("query 7: #################################################################################")

T_7 = datetime.datetime.now()

projs_three = copy.deepcopy(RANDOM_PROJS)
projs_three.append("/programs/calypr/projects/testthree")

count = 0
for i in G.query().V().\
    hasLabel("Observation").has(gripql.within("auth_resource_path", projs_three)).\
    as_("f0").unwind("component").as_("f0").outNull("focus_DocumentReference").\
    has(gripql.within("auth_resource_path", projs_three)).\
    as_("f0").outNull("subject_Specimen").\
    has(gripql.within("auth_resource_path", projs_three)).\
    as_("f1").limit(10000).render({
        "focus":{
            "__typename":"DocumentReferenceType",
            "auth_resource_path":"$f0.auth_resource_path",
            "content":"$f0.content",
            "id":"$f0.id",
            "subject":{
                "__typename":"SpecimenType",
                "auth_resource_path":"$f1.auth_resource_path",
                "id":"$f1.id",
                "processing":"$f1.processing"
            }
        }
    }):
    print("I: ", i)
    count += 1
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_7).total_seconds()))


###################################################################################################
# 8.    Calypr 2 traversal + 1 filter query


print("query 8: #################################################################################")
T_8 = datetime.datetime.now()

projs_three = copy.deepcopy(RANDOM_PROJS)
projs_three.append("/programs/calypr/projects/testthree")

count = 0
for i in G.query().V().\
    hasLabel("Observation").has(gripql.within("auth_resource_path", projs_three)).as_("f0").\
    has(gripql.eq("Observation.component.valueString", "Malignant melanoma NOS")).\
    outNull("focus_DocumentReference").has(gripql.within("auth_resource_path", projs_three)).\
    as_("f0").unwind("content").as_("f0").unwind("content.attachment.extension").\
    as_("f0").outNull("subject_Specimen").has(gripql.within("auth_resource_path", projs_three)).\
    as_("f1").select("f0").\
    has(gripql.within("auth_resource_path", projs_three)).totype("$f0.content.attachment.extension","list").\
    group({"content":"$f0.content"}).as_("f0").limit(10000).render({
            "focus":{
                "__typename":"DocumentReferenceType",
                "auth_resource_path":"$f0.auth_resource_path",
                "content":"$f0.content",
                "id":"$f0.id",
                "subject":{
                    "__typename":"SpecimenType",
                    "auth_resource_path":"$f1.auth_resource_path",
                    "id":"$f1.id","processing":"$f1.processing"
                }
            }
        }):
    count += 1
print("Successfully queried %d rows in %.2f seconds" % (count, (datetime.datetime.now() - T_8).total_seconds()))
print()
print("Total Benchmark Time:  %.2f " %  (datetime.datetime.now() - T_LOAD).total_seconds())
