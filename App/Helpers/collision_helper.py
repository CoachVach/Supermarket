def object_collision(objects, rect):
    collisions = []
    for object in objects:
        if object.interface.rect().colliderect(rect):
            collisions.append(object)
    return collisions