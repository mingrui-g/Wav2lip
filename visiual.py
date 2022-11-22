 # spatialOut1 = np.maximum(spatialOut1,0).detach().numpy()
                # min_heat = np.min(spatialOut1.detach().numpy())
                # max_heat = np.max(spatialOut1.detach().numpy())
                # if max_heat == 0:
                #     max_heat = 1e-10
                # spatialOut1 -= min_heat
                # spatialOut1 /= (max_heat-min_heat)

# spatialOut = cv2.applyColorMap(spatialOut, cv2.COLORMAP_AUTUMN)
                # plt.figure()
                # plt.imshow(spatialOut)
                # plt.savefig("spatialOut_AUTUMN.png")

                # spatialOut1 = cv2.applyColorMap(spatialOut1, cv2.COLORMAP_JET)
                # plt.figure()
                # plt.imshow(spatialOut1)
                # plt.savefig("spatialOut_JET.png")

                # spatialOut1 = cv2.applyColorMap(spatialOut1, cv2.COLORMAP_HOT)
                # plt.figure()
                # plt.imshow(spatialOut1)
                # plt.savefig("spatialOut_HOT.png")