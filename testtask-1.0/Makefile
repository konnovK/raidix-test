TARGET=testtask

all: build

build:
	gcc testtask.c -o $(TARGET)

clean:
	rm $(TARGET)

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 755 $(TARGET) $(DESTDIR)/usr/bin/$(TARGET)

uninstall:
	rm $(DESTDIR)/usr/bin/$(TARGET)
