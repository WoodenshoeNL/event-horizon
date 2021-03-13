# Dir

## Search for file in all sub-directories and only show file

```cmd
dir /s /b passwords.txt
```



## Options for DIR

```cmd
[pathname] The drive, folder, and/or files to display,
              this can include wildcards:
                 *   Match any characters
                 ?   Match any ONE character

   [display_format]
   /P   Pause after each screen of data.
   /W   Wide List format, sorted horizontally.
   /D   Wide List format, sorted by vertical column.

   [file_attributes] /A[:]attribute

   /A:D  Folder         /A:-D  NOT Folder
   /A:R  Read-only      /A:-R  NOT Read-only
   /A:H  Hidden         /A:-H  NOT Hidden
   /A:A  Archive        /A:-A  NOT Archive
   /A:S  System file    /A:-S  NOT System file
   /A:I  Not content indexed Files  /A:-I  NOT content indexed
   /A:L  Reparse Point  /A:-L  NOT Reparse Point (symbolic link)

   /A:X  No scrub file  /A:-X  Scrub file    (Windows 8+)
   /A:V  Integrity      /A:-V  NOT Integrity (Windows 8+)

   /A    Show all files
   Several attributes can be combined e.g. /A:HD-R

   [sorted]   Sorted by /O[:]sortorder

   /O:N   Name                  /O:-N   Name
   /O:S   file Size             /O:-S   file Size
   /O:E   file Extension        /O:-E   file Extension
   /O:D   Date & time           /O:-D   Date & time
   /O:G   Group folders first   /O:-G   Group folders last
   several attributes can be combined e.g. /O:GEN

   [time] /T:  the time field to display & use for sorting

   /T:C   Creation
   /T:A   Last Access
   /T:W   Last Written (default)

   [options]
   /S     include all subfolders.
   /R     Display alternate data streams.
   /B     Bare format (no heading, file sizes or summary).
   /L     use Lowercase.
   /Q     Display the owner of the file.

   /N     long list format where filenames are on the far right.
   /X     As for /N but with the short filenames included.

   /C     Include thousand separator in file sizes.
   /-C    Don’t include thousand separator in file sizes.

   /4     Display four-digit years.
          In most recent builds of Windows this switch has no effect.
          The number of digits shown is determined by the ShortDate format
          set in the Control Panel.
```
