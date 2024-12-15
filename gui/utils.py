class FrameManager:
    def __init__(self, root):
        self.root = root
        self.frames = {}

    def add_frame(self, name: str, frame: object):
        self.frames[name] = frame
    
    def remove_frame(self, name: str):
        frame = self.frames.get(name)
        if frame:
            frame.pack_forget()

    def switch_to(self, name):
        for _, frame in self.frames.items():
            frame.pack_forget()

        frame_to_show = self.frames.get(name)
        if frame_to_show:
            print(f"switching frame to: {name}")
            frame_to_show.pack(fill="both", expand=True)