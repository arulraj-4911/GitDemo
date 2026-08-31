from playwright.sync_api import Page , expect
import pytest

@pytest.mark.skip
def test_iframes(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames=page.frames
    print("frames:",len(frames))
    page.wait_for_timeout(4000)
    frame1=page.frame_locator("frame[src='frame_1.html']")#method-1 to get frame
    #frame2 = page.frame(url='#document (https://ui.vision/demo/webtest/frames/frame_1)')#to get by url of i frame
    # frame3 = page.frame("name of the frame") # to get frame by frame name but mostly name won't be available for frames
    page.wait_for_timeout(3000)
    input=frame1.locator("input[name='mytext1']")
    input.fill("arulraj")
    expect(input).to_have_value("arulraj")
    page.wait_for_timeout(3000)

def test_inner_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames=page.frames
    print("frames:",len(frames))
    page.wait_for_timeout(4000)
    frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")
    child=frame1.child_frames
    print("child_frames:",len(child))
    inner_frame=child[0]
    page.wait_for_timeout(4000)
    boxes=inner_frame.get_by_label("I am a human")
    boxes.check()
    page.wait_for_timeout(4000)



