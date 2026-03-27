# WiiUProductCodes.bin Version History & Hashes

This document catalogs the MD5 hashes and structural formats of the `WiiUProductCodes.bin` file across all known major Title Updates (TUs) for **Minecraft: Wii U Edition**.

As the game evolved, the proprietary binary format shifted to accommodate new padding alignments and DLC product parameters.

### Format Timeline
- **v48 – v144**: `Legacy (v1)` format. Highly unoptimized, heavily padded, and entries lack `Code` identifiers.
- **v161 – v464**: `Intermediate (v1.5)` format. Mid-generation transition. Introduces `Unk1/Unk2` header flags and serializes item structs but critically lacks `Index ID` fields.
- **v480 – v688**: `Modern (v2)` format. Fully contiguous, serialized structure utilized for the remainder of the console's lifespan.

---

## Known Versions & MD5 Hashes

| Title Update | MD5 Hash                           | Format Type |
|--------------|------------------------------------|-------------|
| **v48**      | `e61ed2d28a67cb347421c2f18a332ead` | Legacy (v1) |
| **v64**      | `6d297a770e06324eec6874caa64d21f6` | Legacy (v1) |
| **v80**      | `6d297a770e06324eec6874caa64d21f6` | Legacy (v1) |
| **v96**      | `6d297a770e06324eec6874caa64d21f6` | Legacy (v1) |
| **v112**     | `95defb6d260a71d3e8a0b21214f7fa5e` | Legacy (v1) |
| **v128**     | `95defb6d260a71d3e8a0b21214f7fa5e` | Legacy (v1) |
| **v144**     | `95defb6d260a71d3e8a0b21214f7fa5e` | Legacy (v1) |
| **v161**     | `9f5b7aa35e11ce4ab3bb88f56400be2f` | Intermediate (v1.5) |
| **v176**     | `22d10f36e04328107ef97b1913fa0809` | Intermediate (v1.5) |
| **v192**     | `22d10f36e04328107ef97b1913fa0809` | Intermediate (v1.5) |
| **v208**     | `fbb35d6fcb92e4f269a8b6ea0cb8447f` | Intermediate (v1.5) |
| **v224**     | `a5c1229595895b84cc2f3b835ee9e1a5` | Intermediate (v1.5) |
| **v240**     | `8a907e5bc93cda4c62b1a4752689a492` | Intermediate (v1.5) |
| **v256**     | `8a907e5bc93cda4c62b1a4752689a492` | Intermediate (v1.5) |
| **v272**     | `b833c9e620ac368eaa9b6fb547b59d41` | Intermediate (v1.5) |
| **v288**     | `cacb22aaa6b000e25fd2ffc6e8a4206b` | Intermediate (v1.5) |
| **v304**     | `cacb22aaa6b000e25fd2ffc6e8a4206b` | Intermediate (v1.5) |
| **v320**     | `1ea4282703aa7977adf443d45d5c6a0f` | Intermediate (v1.5) |
| **v336**     | `1ea4282703aa7977adf443d45d5c6a0f` | Intermediate (v1.5) |
| **v368**     | `d23b9e2bc146a780304d55c02f7a9fcc` | Intermediate (v1.5) |
| **v416**     | `85d134b674de8210ba342a2ff91c3ffc` | Intermediate (v1.5) |
| **v432**     | `7a7f6ebdb2c542e1ad043bfef79896fd` | Intermediate (v1.5) |
| **v448**     | `c1d6bb1f7f34d01fe6d01c96cccd0525` | Intermediate (v1.5) |
| **v464**     | `b4040b2d468d5cb93033afac3dda344b` | Intermediate (v1.5) |
| **v480**     | `1acfc44dd3615f7dae523a06a7c5f209` | Modern (v2) |
| **v496**     | `07e2634641cfa320a2c515cd33732955` | Modern (v2) |
| **v528**     | `35e3b492135c7a8f6aac2415d1f08f66` | Modern (v2) |
| **v544**     | `2a0a3cdc42182b8e141ff0603c2d60c8` | Modern (v2) |
| **v560**     | `3f45fe7c37a519c604c08b793ec1bce2` | Modern (v2) |
| **v592**     | `f8fc58fa73f3e271acd1801ef019a424` | Modern (v2) |
| **v608**     | `f8fc58fa73f3e271acd1801ef019a424` | Modern (v2) |
| **v624**     | `e99b014732f8bc5f92cb7190754bb96e` | Modern (v2) |
| **v640**     | `9561b1972b1336bfccca4c09e806a538` | Modern (v2) |
| **v656**     | `9561b1972b1336bfccca4c09e806a538` | Modern (v2) |
| **v688**     | `d1f972b5293e32d439526780b225b72a` | Modern (v2) |