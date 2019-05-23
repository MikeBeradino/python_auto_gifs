from PIL import Image, ImageSequence


im = Image.open('automata_gif.gif')
frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
frames.reverse()

frames[0].save('reversed.gif', save_all=True, append_images=frames[1:])