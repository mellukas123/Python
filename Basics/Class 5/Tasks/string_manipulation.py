text = "Cupcake ipsum dolor sit amet I love halvah cotton candy I love. Bear claw I love croissant I love pie sesame snaps marshmallow marshmallow bonbon. Sesame snaps candy canes wafer dragée danish. Ice cream jujubes tiramisu I love pudding carrot cake icing jelly tart."

def modify(orginal):
    return orginal.replace(" ", "_").lower()



print(modify(text))