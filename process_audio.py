from mido import MidiFile
from pydub import AudioSegment


def extract_notes(audiopath: str):
    """
    read .mid or .mp3 file and return array of notes
    mido library: https://mido.readthedocs.io/en/latest/
    pydub library: http://pydub.com/
    """

    # read .mid
    if ".mid" in audiopath:
        mid = MidiFile(audiopath)

        notes = []
        for msg in mid:
            if not msg.is_meta and msg.channel == 0 and msg.type == "note_on":
                data = msg.bytes()
                notes.append(data[1])

    # read .mp3
    if ".mp3" in audiopath:
        notes = AudioSegment.from_mp3(audiopath)

    return notes


# def prepare_sequences(seq_length: int):
#     """"""

#     seq_in = []
#     seq_out = []

#     for i in range(len(notes) - seq_length):
#         seq_in.append(notes[i : i + seq_length])
#         seq_out.append(notes[i + seq_length])

#     # TODO: apply some sort of scaler
#     # TODO: make sure the format matches GAN input
#     return (seq_in, seq_out)
