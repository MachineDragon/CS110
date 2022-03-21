import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pic = picture(sys.argv[4])
    prev = BlobFinder(pic, tau)
    prevBlobs = prev.getBeads(P)
    for i in range(5, len(sys.argv)):
        cur = BlobFinder(picture(sys.argv[i]), tau)
        curBlobs = cur.getBeads(P)
        # Take one blob from previous, take one blob from current
        for pBlob in prevBlobs:
            nearest = float('Inf')
            for cBlob in curBlobs:
                # copute distance between pBlob and cBlob
                dist = pBlob.distanceTo(cBlob)
                if dist < nearest:
                    nearest = dist
            if nearest <= delta:
                stdio.writef('%4f\n', nearest)
    stdio.writeln()


if __name__ == '__main__':
    main()
