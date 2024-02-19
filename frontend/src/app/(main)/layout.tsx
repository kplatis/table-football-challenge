import { Container } from '@mantine/core'

export default function MainPagesLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <Container>{children}</Container>
}
