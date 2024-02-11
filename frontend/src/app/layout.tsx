import '@mantine/core/styles.css'

import { ColorSchemeScript, Container, MantineProvider } from '@mantine/core'
import { Header } from '@/components/Header'

export const metadata = {
  title: 'My Mantine app',
  description: 'I have followed setup instructions carefully',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <ColorSchemeScript />
      </head>
      <body>
        <MantineProvider>
          <Container size="md">
            <Header />
            {children}
          </Container>
        </MantineProvider>
      </body>
    </html>
  )
}
