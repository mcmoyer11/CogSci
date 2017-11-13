import itertools

# conditions
conditions = ["spatialGap","pass","launch","slip","independent1"]

# factors for stim selection
# display angles
angles = ["angle0","angle45","angle90","angle135","angle180","angle225","angle270","angle315"]

# stim videos
stim_videofiles = ["{}_{}.mp4".format(x,y) for x in conditions for y in angles]

# # #
# pairings
paired_conditions = list(itertools.combinations(conditions,r=2)) + [(x,x) for x in conditions]
# print(paired_conditions)

# video attributes for familiarization
# order of appearance
# and side on which they appear
order_and_side = [
    ((1, 'L'), (2, 'R')),
    ((1, 'R'), (2, 'L')),
    ((2, 'L'), (1, 'R')),
    ((2, 'R'), (1, 'L'))
]

stim = [((x),(y)) for x in paired_conditions for y in order_and_side]

print(stim, '\n')
print(stim_videofiles)
