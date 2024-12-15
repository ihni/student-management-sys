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
        for frame_name, frame in self.frames.items():
            if frame_name == name:
                print(f"switching frame to: {frame_name}")
                frame.pack(fill="both", expand=True)
            else:
                frame.pack_forget()