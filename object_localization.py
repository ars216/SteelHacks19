import keywords

def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    #print('Number of objects found: {}'.format(len(objects)))
    name_vertex_dict = {}
    #names_list = []
    
    for object_ in objects:
        vertices_list = []
        #print('\n{} (confidence: {})'.format(object_.name, object_.score))
        #names_list.append(object_.name)
        #print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            #print(' - ({}, {})'.format(vertex.x, vertex.y))
            vertices_list.append(vertex.x)
            vertices_list.append(vertex.y)
        #print("vertices_list=", vertices_list)
        name_vertex_dict[object_.name] = vertices_list

    return(name_vertex_dict)

object_dict1 = (localize_objects("C:\\Users\\quiet\\OneDrive\\Documents\\Hackathon!\\SteelHacks19\\powerPlantTL.jpeg"))
object_dict2 = (localize_objects("C:\\Users\\quiet\\OneDrive\\Documents\\Hackathon!\\SteelHacks19\\powerPlantBL.jpeg"))
object_dict3 = (localize_objects("C:\\Users\\quiet\\OneDrive\\Documents\\Hackathon!\\SteelHacks19\\powerPlantTR.jpeg"))
object_dict4 = (localize_objects("C:\\Users\\quiet\\OneDrive\\Documents\\Hackathon!\\SteelHacks19\\powerPlantBR.jpeg"))
'''
print("dict1=", object_dict1)
print("dict2=", object_dict2)
print("dict3=", object_dict3)
print("dict4=", object_dict4)
'''
keywords.keywords(object_dict1, object_dict2, object_dict3, object_dict4)